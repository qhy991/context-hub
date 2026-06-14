---
name: opt-rdna-apu-moe-matmul
description: "Optimizing MoE / quantized matmul (MUL_MAT / MUL_MAT_ID) on RDNA3.5 APU (gfx1151) — the ~70%-of-decode P0 bottleneck: bandwidth-bound GEMV at decode vs WMMA-able compute-bound GEMM at prefill, low-bit quant and dequant-on-the-fly."
metadata:
  languages: hip
  architectures: rdna3_5
  versions: 'RDNA3.5'
  revision: 1
  updated-on: '2026-06-14'
  source: community
  tags: rocm,gpu,optimization,rdna3_5,gfx1151,apu,moe,matmul,gemv,quantization,bandwidth-bound,decode
  isa_category: optimization
  instruction_type: guide
  hw_unit: simd-unit
---

# MoE / Quantized Matmul on RDNA3.5 APU — The Real P0

A worked guide to the kernel that actually matters at decode on gfx1151
(Ryzen AI Max+ 395 / Radeon 8060S): **quantized matmul** — `MUL_MAT` (dense
projections, FFN, `lm_head`) and `MUL_MAT_ID` (MoE expert FFN). Per in-house
profiling of **Qwen3.5-35B-A3B** (Q4_K_M) decode, these are **~70% of decode
time** and KV-length-independent. This is the **P0** target — the opposite
altitude lesson to the sibling flash-attention study, where the FA kernel is only
**~0.6%** of decode and six optimization sessions produced no end-to-end win (see
[[opt-rdna-apu-flash-attention]]).

> **Provenance**: hardware facts are RDNA3.5 / AMD-published. The decode op
> breakdown, micro-benchmarks, and the P0–P4 priority list are *measured* in
> `AKW-Exp/exp-amd-395` (exp-amd-395, 2026-06-10); all P0–P4 percentage gains are
> **explicit estimates**, kept tagged below. The general decode-vs-prefill
> roofline framing is well-established external roofline literature; the
> gfx1151-specific decode dominance is in-house. No NCU/hardware counters were
> available on this APU stack — bottlenecks are inferred from arithmetic
> intensity and cross-configuration convergence.

## Hardware Context

The part is **gfx1151**, RDNA3.5, **40 RDNA3.5 compute units**, wave32-native,
with **unified LPDDR5X-8000 on a 256-bit bus = 256 GB/s theoretical** shared with
the 16-core Zen 5 CPU (AMD product spec; see [[arch-amd-395-soc]],
[[arch-rdna35-apu]]). Community-measured achievable bandwidth on this platform is
**≈ 212 GB/s** of the 256 GB/s theoretical (rocm_bandwidth_test, llm-tracker.info)
— use 256 GB/s as the roofline denominator unless an achievable figure is needed.

RDNA3.5 has **no CDNA Matrix Core and no `v_mfma_*`**; matrix acceleration is
**WMMA** (cooperative across a wavefront on the SIMD/vector ALUs), tiles
16×16×16, inputs f16/bf16/iu8/iu4 (no FP8 on RDNA3.5). See [[arch-rdna35-wmma]].

> **CU count, resolved**: The full Ryzen AI Max+ 395 / Radeon 8060S has **40
> RDNA3.5 CUs** (vendor spec); the decode op-breakdown run cited here was on the
> full part. The flash-attention optimization *sessions* recorded the GPU as
> "20 CU" — that value belongs to those specific FA sessions (possibly a
> half-enabled or differently-reported config), not to the part. We do not state
> a per-CU SIMD count or any derived peak-FLOP number; the session-derived
> ~TFLOP/s figures rest on uncertain 20-CU + SIMD assumptions and are omitted.

## The Two Regimes: Decode (GEMV) vs Prefill (GEMM)

The central principle — well-established roofline fact (Towards Data Science
"Prefill Is Compute-Bound. Decode Is Memory-Bound."; QServe arXiv:2405.04532):

| Regime | Shape | Bound by | What helps | What WMMA buys |
|--------|-------|----------|------------|----------------|
| **Decode** | `n=1` GEMV / thin GEMM | **Memory bandwidth** — `t ≈ weight_bytes / BW` | fewer weight bytes per token (lower-bit quant, dequant-on-the-fly, read only active experts) | **little** — no weight reuse across the single token, ALUs starve |
| **Prefill / batch** | large `n` GEMM | **Compute** | WMMA, LDS tiling, weight reuse across tokens | **a lot** — matrix-matrix work is the WMMA-able path |

At decode, each weight is read **once** to produce one output column, so
arithmetic intensity is low and the kernel is **bandwidth-bound**: the
roofline runtime is essentially `weight_bytes / BW`. WMMA cannot help — there is
no reuse to amortize the matrix pipe. At prefill (or any batched `n`), the same
weight tile serves many tokens, intensity rises, and the workload becomes
**compute-bound** matrix-matrix multiply — the regime where WMMA, tiling, and
weight reuse pay off.

Corroborating in-house: every measured `MUL_MAT` / `MUL_MAT_ID` config below is
`n=1` (decode GEMV), and the op-breakdown describes them as "memory-bound
quantized GEMM" (exp-amd-395). There is **no separate measured arithmetic-
intensity number for the MoE matmul** — it is bandwidth-bound for the
weight-streaming reason, stated qualitatively. (The `≈ 0.031 FLOPs/byte` figure
in the experiment files belongs to flash attention, not to this kernel.)

## Decode Levers (the bandwidth-bound regime)

The only thing that moves a bandwidth-bound GEMV is **bytes of weight streamed
per token**. Three levers, all reducing memory traffic:

1. **Minimize weight bytes — lower-bit quantization.** INT4 weights are ~4×
   smaller than FP16, so ~4× less weight data is streamed per token. The measured
   workload uses **Q4_K_M**. This is the direct win in the roofline `weight_bytes
   / BW`. (QServe / ATOM roofline literature.)
2. **Dequant-on-the-fly / integer MMQ.** Fuse dequantization into the matmul
   (MMQ / `mul_mat_q`) instead of expanding weights to FP16 first. This avoids
   materializing FP16 weights and reduces memory loads and pointer arithmetic —
   "dequantization is fused with matrix multiplication, reducing the frequency of
   memory loads" (llama.cpp MMQ literature). This is precisely the **P0** target:
   the gfx1151 MoE `MUL_MAT_ID` q4_K MMQ kernel.
3. **MoE reads only active experts.** `MUL_MAT_ID` gathers only the routed
   experts' weights (the measured config routes **8 of 128** experts — see model
   note below), so routing/packing quality directly sets how many weight bytes
   hit the bus. Good gather/packing keeps the active-expert weights contiguous and
   minimizes wasted reads.

The bandwidth ceiling itself is fixed by the **unified LPDDR5X pool** shared with
the CPU — see [[arch-rdna35-unified-memory]] for the memory model that sets this
roofline. No amount of compute scheduling moves a kernel that is already at
`weight_bytes / BW`.

> **Model-config note**: the in-house `MUL_MAT_ID` micro-bench routed **8 of 128**
> experts as benchmarked; we report that measured config and do not assert a
> canonical public expert count. "A3B" = ~3B active params of ~35B total (MoE).

## Prefill Levers (the compute-bound regime)

When you batch (prefill, or `n>1`), the matmul becomes compute-bound and the
WMMA path opens up:

1. **Use WMMA for f16/bf16 matrix-matrix.** RDNA3.5 WMMA (16×16×16, wave32) is
   the matrix-acceleration path — there is **no MFMA** here. See
   [[arch-rdna35-wmma]]. Inputs f16/bf16/iu8/iu4; no FP8 on RDNA3.5.
2. **LDS tiling to reuse weight tiles across tokens — but mind occupancy.** On
   this APU **+1 KB LDS ≈ −4 to −5% latency** (measured occupancy cost). Big
   staging tiles and double-buffering can net-regress; size tiles for occupancy,
   not just reuse.
3. **Respect wave32 semantics.** Code ported from CDNA must not assume a 64-lane
   wavefront; cross-lane / shuffle / WMMA fragment layouts differ. See
   [[opt-hip-vs-cuda-gotchas]].
4. **Avoid LDS bank conflicts** in the staging tile — see
   [[opt-bank-conflict-avoidance]] for the padding/swizzle patterns (note that
   doc's bank model is written for CDNA; the conflict principle carries, the
   wavefront width does not).

## In-House Numbers

Measured on Radeon 8060S gfx1151, ROCm/HIP, warm steady-state (exp-amd-395):

| Metric | Value | Note |
|--------|-------|------|
| End-to-end decode | **24.74 tokens/s = 40.4 ms/token** | llama-bench, kv≈4096 |
| `MUL_MAT` q4_K, m=4096, n=1, k=14336 | **103.64 µs** | big FFN, decode GEMV |
| `MUL_MAT_ID` q4_K, m=768, n=1, k=2048, 8/128 experts | **25.63 µs** | MoE gate/down |
| FLASH_ATTN_EXT hsk=256, kv=4096, F16 | 23.16 µs | for contrast (the 0.6% kernel) |
| GATED_DELTA_NET 32 heads, d=128 | 9.15 µs | linear-attn, for contrast |

Decode op-time breakdown (kv≈4096):

| Op family | Share of decode | KV-dependent? |
|-----------|-----------------|---------------|
| `MUL_MAT` + `MUL_MAT_ID` (MoE FFN + QKV + lm_head) | **~70%** | no — the P0 |
| RMS_NORM + ROPE | ~15–20% | no |
| Elementwise | ~8–10% | no |
| SSM_CONV | ~2.5% | partial |
| GATED_DELTA_NET | ~0.7% | mildly |
| FLASH_ATTN_EXT | ~0.6% (→ ~6–7% only near kv≈64k) | **yes** |

Model: 40 layers = 30 GATED_DELTA_NET (linear-attn) + 10 full FLASH_ATTN_EXT,
`full_attention_interval=4`, hidden d=2048.

## Priority List (gains are ESTIMATES)

The ranking is measured; the percentage gains are **explicit estimates** from the
profiler (exp-amd-395) — keep the "estimate" tag:

| Pri | Target | Est. end-to-end gain |
|-----|--------|----------------------|
| **P0** | MoE `MUL_MAT_ID` q4_K kernel (gfx1151 MMQ) | **5–15%** *(ESTIMATE)* |
| **P1** | QKV `MUL_MAT` 8192×2048 projection | **3–8%** *(ESTIMATE)* |
| **P2** | fused RMS_NORM / norm+rope | **2–5%** *(ESTIMATE)* |
| **P3** | FLASH_ATTN_EXT (only kv>16k) | **1–3%** *(ESTIMATE)* |
| **P4** | GATED_DELTA_NET | **<1%** at kv=4096 *(ESTIMATE)* |

The 5–15% P0 figure is the *expected* payoff of a better MMQ kernel; it is not a
measured speedup. Do not quote it as one.

## What NOT To Do (bandwidth-bound traps)

Carried from the flash-attention ledger ([[opt-rdna-apu-flash-attention]]) — the
same DDR5-bandwidth ceiling governs the decode GEMV:

- **Don't reach for WMMA at decode.** With `n=1` there is no weight reuse to
  amortize the matrix pipe; WMMA buys little when you are bandwidth-bound. WMMA is
  the **prefill/batch** lever.
- **Don't expand quantized weights to FP16 before the matmul.** That doubles+ the
  bytes streamed per token — the exact opposite of the decode lever. Fuse dequant
  into the matmul (MMQ).
- **Don't trade LDS/occupancy for staging at decode.** +1 KB LDS ≈ −4 to −5%
  latency here; big staging tiles regress a kernel that is already memory-bound.
- **Don't micro-optimize ILP/unroll expecting a roofline break.** On a kernel at
  `weight_bytes / BW`, scheduling tweaks have a hard ceiling near 1.0x — the FA
  study reached only 1.008x and correctly stalled. Reduce *bytes*, not cycles.
- **Don't pick a kernel without checking its end-to-end weight first.** FA is
  ~0.6% of decode; matmul is ~70%. Gate kernel selection on the op breakdown.
- **Don't cold-benchmark.** Warm up (cold ≈ 7 µs vs steady ≈ 74 µs on the FA
  shape) and expect a ~1% run-to-run noise floor on shared DDR5.

## See Also

- [[opt-rdna-apu-flash-attention]] — sibling bandwidth-bound case study and the
  altitude lesson (the 0.6% kernel)
- [[arch-rdna35-apu]] — the APU that forces the bandwidth ceiling
- [[arch-rdna35-unified-memory]] — the unified memory pool that sets the roofline
- [[arch-rdna35-wmma]] — the WMMA path for the compute-bound prefill regime
- [[opt-hip-vs-cuda-gotchas]] — wave32 / portability footguns
- [[opt-bank-conflict-avoidance]] — LDS bank model for the staging tile
- [[arch-amd-395-soc]] — the SoC-level part overview

## References

- `AKW-Exp/exp-amd-395/20260610-op-breakdown.md` — decode op breakdown, micro-benchmarks, priority list
- `AKW-Exp/exp-amd-395/20260611-175052/methodology-review.md` — bandwidth-bound reasoning, no-NCU note
- "Prefill Is Compute-Bound. Decode Is Memory-Bound." (Towards Data Science)
- [QServe: W4A8KV4 Quantization (arXiv:2405.04532)](https://arxiv.org/pdf/2405.04532)
- [llama.cpp MMQ fused dequant (Emergent Mind)](https://www.emergentmind.com/topics/llama-cpp)
- [Strix Halo / Ryzen AI Max+ 395 GPU Performance (llm-tracker.info)](https://llm-tracker.info/AMD-Strix-Halo-(Ryzen-AI-Max+-395)-GPU-Performance)
