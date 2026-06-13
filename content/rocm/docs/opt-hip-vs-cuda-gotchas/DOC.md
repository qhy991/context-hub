---
name: opt-hip-vs-cuda-gotchas
description: "HIP-vs-CUDA optimization gotchas: tricks that help on NVIDIA but regress or no-op on AMD HIP — __expf, #pragma unroll, double-buffering, wave32, plus APU benchmarking hazards."
metadata:
  languages: hip
  architectures: rdna3_5,cdna3,cdna4
  versions: 'ROCm 6.0+'
  revision: 1
  updated-on: '2026-06-13'
  source: community
  tags: rocm,gpu,optimization,hip,cuda,portability,anti-pattern,gotcha,benchmarking
  isa_category: optimization
  instruction_type: guide
  hw_unit: simd-unit
---

# HIP vs CUDA Optimization Gotchas

A field guide to optimizations that are **correct intuition on NVIDIA/CUDA but
backfire on AMD/HIP**. Agents porting CUDA kernels (or applying CUDA-trained
habits) repeatedly lose time here.

> **Provenance**: each item below was *measured* on gfx1151 (RDNA3.5 APU) in the
> `AKW-Exp/exp-amd-395` flash-attention sessions. Magnitudes are part-specific;
> the **direction** (help vs regress vs no-op) is the portable lesson. Confirm on
> your target before relying on a magnitude.

## Anti-Patterns (measured)

| CUDA habit | HIP / AMD result | Why |
|------------|------------------|-----|
| `__expf` (fast-math intrinsic) | **~5% regression** vs `expf` | The HIP fast-path is not faster here; the "approximate" intrinsic costs more on this ISA. |
| `#pragma unroll` to force unrolling | **no effect** | hipcc/LLVM already unrolls these loops; the pragma is redundant, not a control knob. |
| `__launch_bounds__(N, 1)` | **no effect**; `(128, 2)` *did* help | The min-blocks-per-CU argument matters — raising it to request more occupancy helped; the default-ish `1` did not. |
| Double-buffer the K/V tile in LDS | **0.71x** (+8.6 KB LDS) | Extra LDS cuts occupancy; on a bandwidth-bound kernel the occupancy loss dominates the latency-hiding gain. |
| Shrink tile size to raise occupancy | **0.77x** | Same trap: more waves did not offset the lost per-wave work efficiency. |
| Warp specialization (producer/consumer) | **0.76x** | Specialization overhead is not amortized on a memory-bound, low-occupancy APU kernel. |
| Manual cross-lane KQ rewrite via warp shuffle | **build failure** | Wave32 vs wave64 lane assumptions and HIP shuffle semantics differ from CUDA. |

## The Two Root Causes

1. **LDS is precious on the margin.** On RDNA3.5 APU, **every +1 KB of LDS ≈
   −4–5% latency** because it costs occupancy. CUDA's "stage more in shared memory
   to hide latency" reflex regresses on bandwidth-bound AMD kernels. Budget LDS
   like registers, not like scratch. See [[opt-bank-conflict-avoidance]] for the
   LDS bank model.

2. **wave32, not wave64.** RDNA is wave32-native; CDNA is wave64. Cross-lane code
   (shuffles, ballots, reductions) ported from CUDA's 32-lane warp *or* from
   CDNA's 64-lane wavefront can be silently wrong or fail to build. Always check
   `warpSize` / the target wavefront. See [[arch-rdna35-apu]].

## Benchmarking Hazards (APU)

- **Warm up first.** The iGPU shares thermal/power with the CPU; a cold kernel
  read **~7 µs** but stabilized at **~74 µs**. Cold-start numbers are meaningless.
- **Know your noise floor.** Baseline latency varied **~1%** run-to-run on shared
  DDR5 (thermal + CPU contention). **Sub-1% speedup claims are inside the noise**
  — do not report them as wins without a warmed, repeated protocol.
- **No NCU / hardware counters** on the Windows APU stack. Classify bottlenecks by
  **arithmetic intensity** + cross-configuration measurement convergence, not
  profiler counters.

## Things That Did Transfer

- `__launch_bounds__(128, 2)` + modest VKQ register unroll (4x) — the only net win
  found, and small (~1.008x) because the kernel was already at its bandwidth
  ceiling. ILP/register tuning is still the right *first* lever; just expect it to
  hit a wall fast on memory-bound kernels.

## See Also

- [[arch-rdna35-apu]] — why this part is bandwidth-bound
- [[opt-rdna-apu-flash-attention]] — full case study and the measured-out ledger
- [[opt-bank-conflict-avoidance]] — LDS bank model (CDNA + RDNA)

## References

- [HIP Porting Guide](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html)
- [HIP Programming Guide — Performance](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/performance_guidelines.html)
- `AKW-Exp/exp-amd-395/20260612-195934/state.md` — measured-out strategy ledger
