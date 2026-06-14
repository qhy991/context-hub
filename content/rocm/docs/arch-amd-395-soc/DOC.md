---
name: arch-amd-395-soc
description: "AMD Ryzen AI Max+ 395 (Strix Halo) SoC: 16-core Zen 5 CPU, Radeon 8060S (40 RDNA3.5 CUs / gfx1151), XDNA 2 NPU (~50 TOPS), unified LPDDR5X-8000 256-bit ~256 GB/s — and what each block means for ROCm kernel work."
metadata:
  languages: hip
  architectures: rdna3_5
  versions: 'RDNA3.5'
  revision: 1
  updated-on: '2026-06-14'
  source: community
  tags: rocm,gpu,architecture,rdna3_5,gfx1151,amd-395,strix-halo,apu,radeon-8060s,zen5,xdna2
  isa_category: architecture
  instruction_type: guide
  hw_unit: simd-unit
---

# AMD Ryzen AI Max+ 395 ("Strix Halo") SoC

Full-SoC reference for the **AMD Ryzen AI Max+ 395** (codename *Strix Halo*): a
single TSMC N4 package combining a 16-core Zen 5 CPU, the **Radeon 8060S** iGPU
(40 RDNA3.5 CUs, `gfx1151`), an XDNA 2 NPU, and one **unified LPDDR5X** memory
pool shared by all three. For ROCm/HIP kernel work, only the GPU block is a
programmable target — but the unified memory and the shared power budget shape
how every kernel behaves. This entry catalogs the SoC and maps each block to its
kernel-engineering consequence.

> **Provenance**: SoC block specs (cores, clocks, cache, CU count, shaders, NPU
> TOPS, memory bus, process, cTDP) are **VENDOR-published** (AMD product page,
> Notebookcheck, Tom's Hardware) — stated plainly below. Achievable-bandwidth and
> inference-throughput figures are **COMMUNITY-MEASURED** (llm-tracker.info Strix
> Halo page) — attributed, not vendor spec. One end-to-end decode number is
> **IN-HOUSE-MEASURED** on this exact part (`AKW-Exp/exp-amd-395`). Do not read
> the community/in-house rows as datasheet guarantees.

## SoC Block Spec

| Block | Spec | Notes |
|-------|------|-------|
| **CPU** | 16× Zen 5 cores / 32 threads, up to **5.1 GHz** boost (base **3.0 GHz**) | `[VENDOR]` |
| **CPU cache** | **80 MB total = 16 MB L2 + 64 MB L3** | `[VENDOR]` |
| **GPU** | Radeon 8060S, **40 RDNA3.5 CU**, `gfx1151` | `[VENDOR]` — the ROCm/HIP target |
| **GPU shaders** | **2560** unified shaders (= 40 CU × 64) | `[VENDOR]` |
| **GPU clock** | up to **~2.9 GHz** | `[VENDOR]` (single-source extension; "up to") |
| **GPU matrix** | **WMMA** on the SIMD/vector ALUs — **no dedicated Matrix Core**, no MFMA | `[VENDOR]` |
| **NPU** | XDNA 2, up to **50 TOPS** (INT8) | `[VENDOR]` — separate stack, not a ROCm target |
| **Memory** | **LPDDR5X-8000**, 256-bit bus = **~256 GB/s** theoretical | `[VENDOR]` |
| **Memory capacity** | **32 / 64 / 128 GB**, unified across CPU+GPU+NPU | `[VENDOR]` |
| **Process** | **TSMC N4** (4 nm) | `[VENDOR]` |
| **Power** | configurable TDP **45–120 W** (default **55 W**) | `[VENDOR]` |

GFX-family orientation: RDNA3.5 = `gfx115x`, so the 8060S is `gfx1151`. (RDNA3 =
`gfx110x`, RDNA4 = `gfx120x`; CDNA3 = `gfx940/gfx942`, CDNA4 = `gfx950`.) See
[[arch-amd-gpu-families]] for the full map — this SoC is firmly on the **RDNA**
(consumer/APU) side, not CDNA.

> **NPU TOPS nuance**: the **50 TOPS** figure is the **XDNA 2 NPU alone**. Some
> sources cite **~126 TOPS** as a *chip-level* aggregate (NPU + GPU + CPU). Those
> are different quantities — do not treat 126 as the NPU spec. This entry uses the
> 50-TOPS NPU number.

## What Each Block Means for ROCm / Kernel Work

### GPU (`gfx1151`) — the only ROCm/HIP target

The Radeon 8060S is what HIP compiles for and what ROCm dispatches to. Two
architectural facts dominate kernel design:

- **wave32-native, not wave64.** Cross-lane code and wavefront-width assumptions
  ported from CDNA (wave64-only) are a correctness/perf footgun here. See
  [[opt-hip-vs-cuda-gotchas]].
- **WMMA, not MFMA — there is no dedicated Matrix Core.** Matrix math executes
  cooperatively across a wavefront on the vector ALUs via `__builtin_amdgcn_wmma_*`
  intrinsics (or the portable rocWMMA header API). CDNA `v_mfma_*`-tuned kernels
  do **not** transfer. See [[arch-rdna35-wmma]] for the intrinsic families, tile
  shapes, and fragment layouts, and [[arch-rdna35-apu]] for the broader
  hardware-implication summary.

### NPU (XDNA 2) — not addressable from ROCm/HIP

The XDNA 2 NPU (~50 TOPS INT8) is a **separate accelerator** with its own
software stack (Ryzen AI / XDNA runtime). It is **not** a ROCm device and cannot
be targeted with HIP. For ROCm kernel work it does not exist — treat it as a
distinct platform, not extra GPU throughput.

### Unified memory — the dominant performance factor

CPU, GPU, and NPU share **one LPDDR5X pool** (~256 GB/s theoretical). Unlike an
HBM CDNA part with dedicated device memory, the iGPU's bandwidth-to-FLOP ratio is
low, so low-arithmetic-intensity kernels (decode-time attention, quantized GEMV)
are typically **bandwidth-bound, not compute-bound**. The unified pool is the
single biggest lever on kernel behavior here:

- **Community-measured** (llm-tracker.info Strix Halo page): achievable
  **~212 GB/s of the 256 GB/s** theoretical via `rocm_bandwidth_test`;
  **~84 GB/s** CPU→GPU copy; an example carveout of **8 GB GART + 110 GB GTT** on
  a 128 GB box. Treat these as community figures, not vendor spec.

How much of the pool the GPU may use (GART/GTT split) is configurable and bounds
your working set. See [[arch-rdna35-unified-memory]] for the allocation model and
its kernel implications.

### Thermal / power — one cTDP across CPU+GPU+NPU

All three blocks draw from a **single configurable TDP (45–120 W, default 55 W)**.
CPU and NPU activity directly contends with GPU power, so iGPU clocks (and thus
kernel latency) are sensitive to overall system load and the platform power
setting. Microbenchmarks must warm up and run at steady state; cold/contended
measurements mislead (see the warm-up and noise-floor notes in
[[arch-rdna35-apu]]).

## CU Count: 40, Not 20

**The full Ryzen AI Max+ 395 / Radeon 8060S has 40 RDNA3.5 CUs** (2560 shaders).
Some files under `AKW-Exp/exp-amd-395` say "20 CU" — that figure has **no
hardware-probe basis**:

- It originates in an **LLM-generated flash-attention kernel profile**
  (`exp-amd-395/20260611-175052/kernel-profile.md`, with *NCU Available: false*
  and *Profiler Available: none*) and was then **propagated** into
  `dispatch-args.json`, handoff/transfer JSON, and later-session profiles — an
  agent assumption, never a measured device query.
- The authoritative experiment header records the **full 8060S (gfx1151)**:
  `exp-amd-395/20260610-op-breakdown.md`.
- The earlier [[arch-rdna35-apu]] entry repeats "20 CU (as recorded in
  exp-amd-395 sessions)" — that is the same propagated assumption, not a measured
  config.

**Use 40 CU for the full SoC.** The 20-CU value appears only as an unverified
profile assumption in one flash-attention session, never as a probed config.

## Why This SoC Matters (Performance Anchor)

- **Community-measured** (llm-tracker.info): llama.cpp **Llama-2-7B Q4_0 ~52
  tok/s** text-gen.
- **In-house-measured** (`AKW-Exp/exp-amd-395`, Radeon 8060S `gfx1151`):
  **Qwen3.5-35B-A3B Q4_K_M decode = 24.74 tok/s (40.4 ms/token)** at kv=4096.

These two rates are **not directly comparable** — a 7B dense model versus a
35B-total (~3B-active) MoE — they only bracket the part's text-gen range. Both are
inference workloads that live or die on the unified memory pool — which
is exactly why the memory block, not raw CU count, is the first thing to reason
about when optimizing a kernel for this part. For the op-level breakdown and the
bandwidth-bound case study, see [[opt-rdna-apu-flash-attention]] and
[[opt-rdna-apu-moe-matmul]].

## See Also

- [[arch-amd-gpu-families]] — gfx-id map (RDNA vs CDNA, where gfx1151 sits)
- [[arch-rdna35-apu]] — RDNA3.5 APU hardware implications (wave32, no MFMA, profiling)
- [[arch-rdna35-wmma]] — WMMA intrinsics, tile shapes, fragment layouts on gfx1151
- [[arch-rdna35-unified-memory]] — the unified LPDDR5X pool and GART/GTT model
- [[opt-rdna-apu-flash-attention]] — bandwidth-bound flash attention case study
- [[opt-rdna-apu-moe-matmul]] — the dominant decode op family on this part

## References

- [AMD Ryzen AI Max+ 395 product page](https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo/ryzen-ai-max-plus-395.html)
- [Notebookcheck — Ryzen AI Max+ 395 specs & benchmarks](https://www.notebookcheck.net/AMD-Ryzen-AI-Max-395-Processor-Benchmarks-and-Specs.942323.0.html)
- [Tom's Hardware — Strix Halo launch / unified memory tech](https://www.tomshardware.com/pc-components/cpus/amds-beastly-strix-halo-ryzen-ai-max-debuts-with-radical-new-memory-tech-to-feed-rdna-3-5-graphics-and-zen-5-cpu-cores)
- [llm-tracker.info — Strix Halo GPU Performance (community-measured)](https://llm-tracker.info/AMD-Strix-Halo-(Ryzen-AI-Max+-395)-GPU-Performance)
- `AKW-Exp/exp-amd-395/20260610-op-breakdown.md` — in-house decode measurements
