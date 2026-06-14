---
name: arch-amd-gpu-families
description: "AMD GPU architecture families: RDNA (Radeon/consumer + APU, wave32, WMMA on SIMD ALUs) vs CDNA (Instinct/datacenter, wave64, dedicated MFMA Matrix Cores) — gfx generation map and where Ryzen AI Max+ 395 (RDNA3.5 / gfx1151) sits."
metadata:
  languages: hip
  architectures: rdna3_5,cdna3,cdna4
  versions: 'RDNA1+ / CDNA1+'
  revision: 1
  updated-on: '2026-06-14'
  source: community
  tags: rocm,gpu,architecture,rdna,cdna,gfx,wave32,wave64,family-map,amd-395
  isa_category: architecture
  instruction_type: guide
  hw_unit: simd-unit
---

# AMD GPU Architecture Families: RDNA vs CDNA

A navigation and disambiguation doc. AMD ships **two distinct GPU architecture
lines**, and conflating them is a common source of correctness and performance
bugs when porting kernels. **RDNA** powers Radeon consumer GPUs and APUs
(including the Ryzen AI Max+ 395 / Radeon 8060S iGPU). **CDNA** powers the
Instinct data-center accelerators (the MI100–MI350 series). They differ in
native wavefront width, matrix-acceleration hardware, and memory model. Read
this first to route to the right family-specific entries and to avoid
cross-applying habits from one line to the other.

> **Provenance**: the family split, the per-line defining traits, and the gfx
> generation map are **vendor-published** facts (AMD / GPUOpen / ROCm / LLVM
> docs). The Ryzen AI Max+ 395 identity and its **40 RDNA3.5 CU** count are
> **vendor** facts (AMD blog). One in-house flash-attention profiling session
> recorded a conflicting "20 CU" descriptor; that is **in-house-measured /
> session-stated**, not a vendor spec, and is flagged below. The current ROCm
> docs list **CDNA3 as gfx942** (gfx940 was an early pre-release ID, now
> superseded); this doc follows the current ROCm spec.

## RDNA vs CDNA — Side by Side

| Property | **RDNA** (Radeon / consumer + APU) | **CDNA** (Instinct / data center) |
|----------|------------------------------------|-----------------------------------|
| Positioning | Consumer GPUs and APUs | Data-center accelerators |
| Native wavefront | **wave32** (wave64 also supported) | **wave64 only** |
| Matrix engine | **WMMA** (Wave Matrix Multiply-Accumulate), executed cooperatively across the wavefront **on the SIMD/vector ALUs** — **no dedicated matrix-core block** | **Dedicated Matrix Cores** with **MFMA** instructions (`v_mfma_*`) |
| Matrix precision note | RDNA3/RDNA3.5 WMMA does **not** support FP8 (FP8 WMMA + sparsity arrive with RDNA4); **no MFMA path on RDNA** | MFMA, including FP8/FP6/FP4 on the newest parts (see [[arch-cdna4-matrix-core]]) |
| Memory | Unified **DDR5/LPDDR5X** pool shared with the CPU (APUs), or GDDR (discrete Radeon) | Dedicated **HBM** (HBM2e / HBM3) |
| Example products | Radeon RX, Radeon 8060S iGPU (Ryzen AI Max+ 395) | Instinct MI100 / MI200 / MI300 / MI350 |

The single most important takeaway: **RDNA accelerates matrix math on the vector
ALUs via WMMA, while CDNA has dedicated Matrix Cores driven by MFMA.** There is
no `v_mfma_*` path on RDNA, and no WMMA-on-SIMD-ALU model on CDNA.

## gfx Generation Map

**RDNA line** (Radeon / consumer + APU):

| Generation | gfx family | Example IDs |
|------------|-----------|-------------|
| RDNA1 | gfx10.1 | gfx101x |
| RDNA2 | gfx10.3 | gfx103x |
| RDNA3 | gfx11 | gfx1100 / gfx1101 / gfx1102 |
| **RDNA3.5** | **gfx11.5** | **gfx1150 / gfx1151 / gfx1152** |
| RDNA4 | gfx12 | gfx1200 / gfx1201 |

> RDNA3/3.5/4 gfx strings (gfx110x / gfx115x / gfx120x) are confirmed exact.
> The RDNA1/RDNA2 sub-IDs (gfx101x / gfx103x) are given at generation level; the
> generation mapping is confirmed, the exact sub-ID strings are not load-bearing
> here.

**CDNA line** (Instinct / data center):

| Generation | gfx ID | Example product |
|------------|--------|-----------------|
| CDNA1 | gfx908 | MI100 |
| CDNA2 | gfx90a | MI200 / MI250 |
| CDNA3 | **gfx942** | MI300 series |
| CDNA4 | gfx950 | MI350 series |

> CDNA3 is **gfx942** in current ROCm docs. `gfx940` was an early/pre-release ID
> that has been superseded — do **not** target gfx940 as a current ID.

## Where the AMD Ryzen AI Max+ 395 Sits

The **AMD Ryzen AI Max+ 395** (codename **Strix Halo**) is firmly on the **RDNA
side**:

| Attribute | Value |
|-----------|-------|
| Architecture | **RDNA3.5** |
| GFX ID | **gfx1151** |
| iGPU | **Radeon 8060S** |
| Compute units | **40 RDNA3.5 CUs** (AMD blog) |
| CPU | 16× Zen 5 cores / 32 threads, up to 5.1 GHz boost, 80 MB total cache |
| NPU | XDNA 2, up to 50 TOPS (INT8) |
| Memory | LPDDR5X-8000, 256-bit bus = **256 GB/s theoretical**; configs 32/64/128 GB, unified with CPU (up to 96 GB convertible to VRAM via Variable Graphics Memory) |
| Process | TSMC N4 (4 nm) |
| TDP | Configurable 45–120 W |

`gfx1151` is Strix Halo; `gfx1150` is the related Strix Point part. The 395 is
**not** a CDNA part: there are **no Matrix Cores, no MFMA, no HBM** — it is
wave32-native with WMMA on the SIMD ALUs and a single unified DDR5/LPDDR5X pool
shared with the CPU. See [[arch-amd-395-soc]] and [[arch-rdna35-apu]] for the
full SoC and kernel-engineering picture.

> **CU-count caveat (read before quoting a number).** AMD's blog states the
> Radeon 8060S is "driven by 40 AMD RDNA 3.5 CUs" — the canonical figure is
> **40 CU**. One in-house flash-attention profiling session
> (`AKW-Exp/exp-amd-395/20260611-175052/kernel-profile.md`) records "20 CU" in
> its `GPU Model` field, and a derived note. That **20 CU** value is a
> session-stated descriptor, **not** an AMD spec, and **conflicts with the 40 CU
> vendor figure**; the in-house op-breakdown run
> (`AKW-Exp/exp-amd-395/20260610-op-breakdown.md`) names the full Radeon 8060S
> part (which AMD specs at 40 CU). Treat **40 CU** as canonical; if you cite 20 CU
> at all, attribute
> it explicitly to that single session profile and flag it as inconsistent.

## Do Not Cross-Apply

Kernels and tuning heuristics do **not** transfer across the family line. When
working on an RDNA part (like the 395 / gfx1151), do **not** carry over CDNA
assumptions, and vice versa:

- **Matrix path.** Do not reach for `v_mfma_*` / MFMA scheduling on RDNA — there
  is no Matrix Core. Use WMMA (see [[arch-rdna35-wmma]]). Conversely, CDNA does
  not run the WMMA-on-SIMD-ALU model.
- **Wavefront width.** RDNA is **wave32-native**; CDNA is **wave64-only**.
  Cross-lane code (shuffles, ballots, reductions) and any hardcoded lane masks
  ported from a 64-lane CDNA kernel are a correctness *and* performance footgun
  on wave32 RDNA. See [[opt-hip-vs-cuda-gotchas]].
- **Memory model / bandwidth.** Do not assume HBM bandwidth on an RDNA APU. The
  395 shares a unified DDR5/LPDDR5X pool with the CPU (256 GB/s theoretical),
  which gives a far lower bandwidth-to-FLOP ratio than an HBM CDNA part — many
  decode kernels are DDR5-bandwidth-bound there (see
  [[arch-rdna35-unified-memory]] and [[arch-rdna35-apu]]).
- **LDS swizzles tuned for 64 lanes.** `ds_read` / LDS swizzle patterns
  hand-tuned for a 64-lane CDNA wavefront do not map cleanly onto a 32-lane RDNA
  wavefront; re-derive the access pattern for wave32 rather than reusing the
  CDNA layout.
- **Precision.** Do not assume FP8 matrix support on RDNA3/RDNA3.5 — it is not
  there (FP8 WMMA + sparsity arrive with RDNA4). FP8/FP6/FP4 are CDNA4 /
  matrix-core features.

## Routing

- **Working on RDNA3.5 / gfx1151 (Ryzen AI Max+ 395 / Radeon 8060S):**
  - [[arch-amd-395-soc]] — full SoC identity (CPU/GPU/NPU/memory)
  - [[arch-rdna35-apu]] — APU compute organization and bandwidth-bound behavior
  - [[arch-rdna35-wmma]] — the WMMA matrix path (the RDNA matrix engine)
  - [[arch-rdna35-unified-memory]] — the unified DDR5/LPDDR5X memory model
  - [[opt-rdna-apu-flash-attention]] — a worked RDNA-APU optimization case study
- **Working on CDNA3 / CDNA4 (Instinct MI300 / MI350):**
  - [[arch-cdna3-matrix-core]] — CDNA3 (gfx942 / MI300) matrix core
  - [[arch-cdna4-matrix-core]] — CDNA4 (gfx950 / MI350) matrix core
  - [[opt-mfma-scheduling]] — scheduling the MFMA Matrix Core pipes
- **Porting between families:** [[opt-hip-vs-cuda-gotchas]] — wave32/wave64 and
  portability footguns.

## See Also

- [[arch-amd-395-soc]]
- [[arch-rdna35-apu]]
- [[arch-rdna35-wmma]]
- [[arch-rdna35-unified-memory]]
- [[arch-cdna3-matrix-core]]
- [[arch-cdna4-matrix-core]]
- [[opt-mfma-scheduling]]
- [[opt-hip-vs-cuda-gotchas]]

## References

- [AMD Ryzen AI Max+ 395 blog (40 CU, CPU/NPU/memory)](https://www.amd.com/en/blogs/2025/amd-ryzen-ai-max-395-processor-breakthrough-ai-.html)
- [ROCm GPU architecture specs (gfx ID ↔ arch map, CDNA3 = gfx942)](https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html)
- [LLVM AMDGPU backend usage (gfx generation IDs)](https://llvm.org/docs/AMDGPUUsage.html)
- [GPUOpen — AMD GPU architecture programming documentation (RDNA ISA / WMMA)](https://gpuopen.com/amd-gpu-architecture-programming-documentation/)
- [wccftech — gfx1151 = Strix Halo / RDNA3.5 ROCm confirmation](https://wccftech.com/amd-strix-point-halo-gfx1151-strix-point-gfx1150-apus-rocm-rdna-3-5-igpu-confirmed/)
- In-house: `AKW-Exp/exp-amd-395/20260610-op-breakdown.md` (40 CU header) and `AKW-Exp/exp-amd-395/20260611-175052/kernel-profile.md` (disputed 20 CU descriptor)
