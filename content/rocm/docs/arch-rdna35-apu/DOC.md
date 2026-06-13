---
name: arch-rdna35-apu
description: "RDNA3.5 APU (gfx1151 / Ryzen AI Max+ 395, Radeon 8060S): unified DDR5/LPDDR5X memory, wave32, no CDNA Matrix Core, bandwidth-bound behavior and no hardware-counter profiling."
metadata:
  languages: hip
  architectures: rdna3_5
  versions: 'RDNA3.5'
  revision: 1
  updated-on: '2026-06-13'
  source: community
  tags: rocm,gpu,architecture,rdna3_5,gfx1151,apu,bandwidth-bound,wave32
  isa_category: architecture
  instruction_type: guide
  hw_unit: simd-unit
---

# RDNA3.5 APU Architecture (gfx1151)

Hardware overview and kernel-engineering implications for the RDNA3.5 APU
(gfx1151 — Ryzen AI Max+ 395 / Radeon 8060S iGPU). Unlike the CDNA data-center
parts (MI100–MI350X), this is a **consumer APU** that shares a single
DDR5/LPDDR5X memory pool with the CPU, which dominates kernel behavior.

> **Provenance**: hardware basics are RDNA3.5 documented facts; the tuning
> constants and bottleneck classification are *measured* on this part in the
> `AKW-Exp/exp-amd-395` flash-attention sessions (2026-06-09 → 06-12). Treat the
> measured rows as gfx1151-specific evidence, not vendor-published numbers.

## Compute Organization

| Property | RDNA3.5 APU (gfx1151) | Contrast: CDNA |
|----------|----------------------|----------------|
| GFX ID | gfx1151 | gfx908–gfx950 |
| Native wavefront | **wave32** (wave64 also supported) | wave64 only |
| Matrix engine | WMMA (wave matrix), **no CDNA MFMA** | dedicated Matrix Cores (`v_mfma_*`) |
| Memory | **unified DDR5/LPDDR5X, shared with CPU** | dedicated HBM2e/HBM3 |
| Compute units (exp config) | 20 CU (as recorded in exp-amd-395 sessions) | 104–304 CU |
| Hardware counters / NCU | **unavailable** on this Windows APU stack | rocprof / rocprofv3 |

## Why This Architecture Is Bandwidth-Bound

The shared DDR5 pool gives this APU a far lower bandwidth-to-FLOP ratio than an
HBM CDNA part. For low-arithmetic-intensity kernels (decode-time attention,
quantized GEMV), the kernel is **DDR5-bandwidth-bound**, not compute-bound:

- Flash attention at DKQ=DV=256, decode (nb=1) measured **arithmetic intensity
  ≈ 0.031 FLOPs/byte** → micro-optimization ceiling is ~1.0x; closing further
  gaps requires *algorithmic memory-traffic reduction*, not ILP/occupancy tuning.
- **Occupancy loss dominates** on bandwidth-bound kernels here: strategies that
  trade LDS/registers for more waves regress (see [[opt-rdna-apu-flash-attention]]).

## Kernel-Engineering Implications

1. **LDS is expensive on the margin** — each **+1 KB of LDS ≈ −4–5% latency**
   (measured). Double-buffering and big staging tiles often net-regress.
2. **wave32, not wave64** — kernels and cross-lane code ported from CDNA must not
   assume a 64-lane wavefront. This is a correctness/perf footgun (see
   [[opt-hip-vs-cuda-gotchas]]).
3. **No Matrix Core** — there is no `v_mfma_*` path; matrix acceleration goes
   through WMMA. CDNA MFMA-tuned kernels do not transfer.
4. **No hardware-counter profiling** — bottlenecks must be inferred from
   arithmetic intensity and cross-configuration measurement convergence.
5. **APU thermal coupling** — the iGPU shares power/thermal budget with the CPU;
   cold-start microbenchmarks mislead (a baseline read ~7 µs cold vs ~74 µs at
   steady state). Always warm up before measuring.

## Profile Before Optimizing (Altitude)

On this APU running Qwen3.5-35B-A3B decode, the end-to-end weight is dominated by
quantized matmul, **not** attention:

| Op family | Share of decode (kv≈4096) |
|-----------|---------------------------|
| MUL_MAT / MUL_MAT_ID (MoE FFN + QKV + lm_head) | **~70%** |
| RMS_NORM / ROPE | ~18% |
| Elementwise | ~9% |
| FLASH_ATTN_EXT | **~0.6%** (rises to ~6–7% only at kv≈64k) |
| GATED_DELTA_NET | ~0.7% |

Optimizing a 0.6% kernel cannot move end-to-end latency; start from the op
breakdown. See [[opt-rdna-apu-flash-attention]] for the full case study.

## References

- [AMD RDNA3.5 / RDNA ISA Reference](https://gpuopen.com/amd-gpu-architecture-programming-documentation/)
- [ROCm on Radeon / Ryzen AI](https://rocm.docs.amd.com/projects/radeon/en/latest/)
- `AKW-Exp/exp-amd-395/20260610-op-breakdown.md` — measured decode op breakdown
- `AKW-Exp/exp-amd-395/20260611-175052/methodology-review.md` — bandwidth-bound analysis
