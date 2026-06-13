---
name: opt-rdna-apu-flash-attention
description: "Case study: optimizing flash attention (DKQ=DV=256) on RDNA3.5 APU (gfx1151) for Qwen3.5-35B-A3B decode — bandwidth-bound ceiling, the measured-out strategy ledger, and the profile-first altitude lesson."
metadata:
  languages: hip
  architectures: rdna3_5
  versions: 'RDNA3.5'
  revision: 1
  updated-on: '2026-06-13'
  source: community
  tags: rocm,gpu,optimization,flash-attention,rdna3_5,gfx1151,apu,bandwidth-bound,decode
  isa_category: optimization
  instruction_type: guide
  hw_unit: simd-unit
---

# Flash Attention on RDNA3.5 APU — Case Study

A worked record of optimizing `fattn-rdna-apu.cuh` (flash attention, DKQ=DV=256)
on gfx1151 for **Qwen3.5-35B-A3B** decode. The headline result is a *negative*
one and it is the point: after six sessions the kernel reached only **1.008x**
against a 1.05x target and the loop correctly **STALLED** — the kernel is
DDR5-bandwidth-bound and micro-optimization cannot close the gap.

> **Provenance**: measured in `AKW-Exp/exp-amd-395` (2026-06-09 → 06-12). All
> speedups are normalized analyzer evidence; no NCU was available (AMD APU).

## Workload

- Model: Qwen3.5-35B-A3B — nh=16, n_head_kv=2 (**GQA=8**), hsk=hsv=256,
  `full_attention_interval=4` → **10 of 40 layers** use full attention
  (the other 30 are GATED_DELTA_NET linear-attention layers).
- Kernel constraint: only modify `fattn-rdna-apu.cuh`, keep the `fattn_kernel_t`
  signature.

## Altitude First: Is This Even Worth Optimizing?

The decode op breakdown (see [[arch-rdna35-apu]]) says **no, not first**:

| kv | FLASH_ATTN_EXT share of decode |
|----|--------------------------------|
| 4,096 | **~0.6%** |
| 16,384 | ~1.8% |
| 64,000 | ~6–7% |

Meanwhile MoE/QKV quantized matmul (`MUL_MAT` / `MUL_MAT_ID`) is **~70%**. A
perfect flash-attention kernel saves <0.6% end-to-end at typical context. **The
lesson: gate kernel selection on its end-to-end weight before entering an
optimization loop** — six sessions on a 0.6% kernel produced no end-to-end win.
The profiler's priority order was P0 MoE matmul, P1 QKV, P2 norm/rope, P3 FA
(only at kv>16k), P4 GDN.

## Why It Is Bandwidth-Bound

Decode (nb=1) flash attention at DKQ=DV=256 has **arithmetic intensity ≈ 0.031
FLOPs/byte**. On a shared-DDR5 APU that puts it firmly in the bandwidth-bound
regime: the ALUs starve waiting on memory, so ILP, unrolling, and tiling have a
hard ceiling near 1.0x. Closing the remaining ~4% needs **algorithmic memory-
traffic reduction** (less KV re-read), not micro-optimization.

## Best Variant Found

`__launch_bounds__(128, 2)` + **4x VKQ register unroll** → **1.008x**
(216.6 µs vs 217.98 µs baseline). Note this is barely above the ~1% measurement
noise floor on this APU.

## Measured-Out Ledger (do not retry on this part)

| Strategy | Result | Lesson |
|----------|--------|--------|
| Reduce tile size (more occupancy) | **0.77x** | Occupancy gain < lost work efficiency |
| Warp specialization | **0.76x** | Overhead not amortized on memory-bound kernel |
| Double-buffer K-tile (+8.6 KB LDS) | **0.71x** | LDS pressure kills occupancy (~4–5%/KB) |
| 8x VKQ unroll | 1.004x | Diminishing vs 4x; register pressure |
| Simple unroll / `#pragma unroll` | no effect | hipcc already unrolls |
| `__launch_bounds__(128, 1)` | no effect | min-blocks arg must request occupancy |
| `__expf` | **−5%** | HIP fast-math intrinsic regresses here |
| Warp-shuffle KQ rewrite | build fails | wave32/shuffle semantics differ |
| Naive causal early-exit | correctness fail (16/2880, nr23=[4,1]) | Edge cases on GQA broadcast |
| V-tile load consolidation | correctness fail | register mapping mismatch |
| KQ 4x consolidated read | no improvement | already bandwidth-bound |

See [[opt-hip-vs-cuda-gotchas]] for the portable version of these findings.

## Promising, Untested

- Corrected `nbatch_fa=64` with proper VKQ rescaling `exp(m_prev − m_max)`
- Q-extent-aware causal early-exit (avoiding the broadcast correctness bug above)
- Split-K across CUs
- Different GQA packing strategy

These are the only remaining levers that change *memory traffic* rather than
compute scheduling — consistent with the bandwidth-bound diagnosis.

## Benchmark Protocol (reproduce)

- **Smoke-test shape first**: `hsk=256,hsv=256,nh=4,nr23=[4,1],kv=512`
  (mask ∈ {0,1}, permute ∈ {[0,1,2,3],[0,2,1,3]}) — three variants tripped here
  before benching.
- **Warm up** (cold ~7 µs vs steady ~74 µs); report only steady-state.
- Build: `cmake --build build-amd --config Release --target test-backend-ops`
- Perf: `test-backend-ops perf -o FLASH_ATTN_EXT -p hsk=256,hsv=256 -b ROCm0`

## See Also

- [[arch-rdna35-apu]] — the hardware that forces the bandwidth ceiling
- [[opt-hip-vs-cuda-gotchas]] — portable HIP-vs-CUDA lessons
- [[opt-bank-conflict-avoidance]] — LDS bank model

## References

- `AKW-Exp/exp-amd-395/20260610-op-breakdown.md` — decode op breakdown
- `AKW-Exp/exp-amd-395/20260611-175052/methodology-review.md` — STALL analysis
- [llama.cpp FlashAttention (ggml)](https://github.com/ggerganov/llama.cpp)
