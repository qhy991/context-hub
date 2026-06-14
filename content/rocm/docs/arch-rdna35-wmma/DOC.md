---
name: arch-rdna35-wmma
description: "RDNA3.5 WMMA matrix engine (gfx1151): Wave Matrix Multiply-Accumulate runs on the SIMD ALUs (no dedicated CDNA Matrix Core) — 16x16x16 tiles, f16/bf16/iu8/iu4 inputs, __builtin_amdgcn_wmma_* intrinsics and rocWMMA, wave32, no FP8 / no MFMA."
metadata:
  languages: hip
  architectures: rdna3_5,rdna3
  versions: 'RDNA3+'
  revision: 1
  updated-on: '2026-06-14'
  source: community
  tags: rocm,gpu,architecture,rdna3_5,rdna3,gfx1151,wmma,matrix,wave32,rocwmma,low-precision
  isa_category: architecture
  instruction_type: guide
  hw_unit: simd-unit
---

# RDNA3.5 WMMA Matrix Engine (gfx1151)

WMMA (**Wave Matrix Multiply-Accumulate**) is AMD's matrix-acceleration path on
RDNA. It was added to GFX11 (RDNA3, `gfx110x`) and carried forward to RDNA3.5
(`gfx115x`, including the Ryzen AI Max+ 395 / Radeon 8060S iGPU, `gfx1151`).
This entry is a reference for the WMMA instruction set, its fragment/VGPR layout,
how to invoke it from HIP, and where it does and does not help.

> **Provenance**: the instruction set, tile size, data types, fragment layout,
> majorness, and packing rules below are **vendor-published** facts from the
> GPUOpen "WMMA on RDNA3" guide (cross-checked against the LLVM clang WMMA
> builtins). The "no MFMA path on gfx1151" and the "WMMA is not always a win on a
> bandwidth-bound APU" notes are **measured in-house** in the
> `AKW-Exp/exp-amd-395` sessions. No absolute RDNA3/3.5 WMMA TFLOPS figure is a
> confirmed vendor fact, so none is quoted here.

## Key Contrast: WMMA Runs on the SIMD ALUs, Not a Matrix Core

This is the single most important architectural fact about WMMA, and the most
common source of confusion when porting from CDNA:

> **On RDNA, WMMA executes cooperatively across the wavefront on the SIMD /
> vector ALUs. There is NO dedicated Matrix-Core block as on CDNA, and there is
> NO `v_mfma_*` (MFMA) instruction path on RDNA.** [VENDOR]

CDNA (Instinct data-center parts) has separate Matrix-Core silicon and a distinct
`v_mfma_*` instruction family (see [[arch-cdna3-matrix-core]] and
[[arch-cdna4-matrix-core]]). RDNA reuses the vector ALUs for matrix math instead.
The practical consequences: MFMA-tuned kernels do not transfer to RDNA, and
matrix work competes with ordinary vector work for the same ALU throughput.
For the broader RDNA-vs-CDNA split see [[arch-amd-gpu-families]]; for the gfx1151
APU context see [[arch-rdna35-apu]].

This was also confirmed in-house: an `exp-amd-395` kernel-profile note records
"RDNA3.5 has no MFMA; wave size is 32; only WMMA for matrix ops" on gfx1151.
[IN-HOUSE-MEASURED] — `AKW-Exp/exp-amd-395/20260612-143745/kernel-profile.md`

| | RDNA3 / RDNA3.5 | CDNA |
|---|-----------------|------|
| Matrix path | WMMA (wave matrix) | MFMA (`v_mfma_*`) |
| Executes on | SIMD / vector ALUs | dedicated Matrix Cores |
| Native wavefront | wave32 (wave64 also supported) | wave64 only |
| GFX IDs | RDNA3 `gfx110x`, RDNA3.5 `gfx115x` (395 = `gfx1151`), RDNA4 `gfx120x` | CDNA1 `gfx908`, CDNA2 `gfx90a`, CDNA3 `gfx940`/`gfx942`, CDNA4 `gfx950` |

## Instruction Families

RDNA3/RDNA3.5 expose **6 WMMA instruction families**, each available in a
**wave32** and a **wave64** form — **12 intrinsics total**. All tiles are
**16×16×16** (M=N=K=16); RDNA3 supports only the 16×16 tile size. Convention:
A is M×K, B is K×N, C/D are M×N (`D = A·B + C`). [VENDOR]

| Family (C,D ← A,B) | A,B inputs | C,D outputs | Tile | wave32 / wave64 builtins |
|--------------------|-----------|------------|------|--------------------------|
| f32 ← f16 | FP16 | FP32 | 16×16×16 | `__builtin_amdgcn_wmma_f32_16x16x16_f16_w32` / `_w64` |
| f32 ← bf16 | BF16 | FP32 | 16×16×16 | `__builtin_amdgcn_wmma_f32_16x16x16_bf16_w32` / `_w64` |
| f16 ← f16 | FP16 | FP16 | 16×16×16 | `__builtin_amdgcn_wmma_f16_16x16x16_f16_w32` / `_w64` |
| bf16 ← bf16 | BF16 | BF16 | 16×16×16 | `__builtin_amdgcn_wmma_bf16_16x16x16_bf16_w32` / `_w64` |
| i32 ← iu8 | IU8 (int8) | I32 | 16×16×16 | `__builtin_amdgcn_wmma_i32_16x16x16_iu8_w32` / `_w64` |
| i32 ← iu4 | IU4 (int4) | I32 | 16×16×16 | `__builtin_amdgcn_wmma_i32_16x16x16_iu4_w32` / `_w64` |

### Data Types

- **Inputs (A, B):** `f16`, `bf16`, `iu8` (int8), or `iu4` (int4).
- **Outputs (C, D):** `f32`, `f16`, `bf16`, or `i32` — per the family table above.

[VENDOR]

## Fragment / VGPR Layout

WMMA operands are held in per-lane register **fragments**. The VGPR cost depends
on operand role and data type, not (for A/B) on wave size: [VENDOR]

| Fragment | VGPRs |
|----------|-------|
| A_frag, B_frag — fp16 / bf16 | **8** (independent of wave size) |
| A_frag, B_frag — iu8 | **4** |
| A_frag, B_frag — iu4 | **2** |
| C_frag, D_frag — wave32 | **8** (regardless of C/D datatype) |
| C_frag, D_frag — wave64 | **4** (regardless of C/D datatype) |

### Majorness and Packing

- **A is column-major; B, C, and D are row-major.** [VENDOR]
- **A and B are packed** — each VGPR packs 2 fp16, 4 iu8, or 8 iu4 values.
- **C and D are unpacked**; `OPSEL` selects which half of the VGPR holds the
  C/D element (`true` → upper half, `false` → lower half). [VENDOR]

Porting note: the column-major A / row-major B convention is the opposite of some
common CUDA layouts — see [[opt-hip-vs-cuda-gotchas]] for the wave32 and layout
footguns when moving matrix code over.

## How to Invoke

### Intrinsic signature

The compiler builtin follows a fixed pattern: [VENDOR]

```
D_frag = __builtin_amdgcn_wmma_<C,D format>_16x16x16_<A,B format>_w<32|64>(
             A_frag, B_frag, C_frag, OPSEL)
```

A minimal HIP sketch for an `f32 ← f16` 16×16×16 tile in wave32 (fragments are
loaded into the appropriately sized VGPR vectors first):

```cpp
// A,B = FP16 (8 VGPRs each, packed); C,D = FP32 (8 VGPRs in wave32)
// A is column-major; B is row-major; C/D are row-major.
using half16  = __attribute__((ext_vector_type(16))) _Float16;
using float8  = __attribute__((ext_vector_type(8)))  float;

__device__ float8 wmma_f16_tile(half16 a_frag, half16 b_frag, float8 c_frag) {
    // OPSEL = false → C/D elements go in the lower half of each VGPR
    return __builtin_amdgcn_wmma_f32_16x16x16_f16_w32(
               a_frag, b_frag, c_frag, /*OPSEL=*/false);
}
```

Compile for the target with `--offload-arch=gfx1151` (or `gfx110x` for RDNA3
discrete). The exact fragment vector widths follow the VGPR table above; for
`f16`/`bf16` outputs only 8 of the 16 output-vector slots carry valid values and
`OPSEL` selects the half — extraction detail that only matters when reading C/D
back element-by-element.

### Portable path: rocWMMA

For portability, prefer **rocWMMA**, a header-only C++ matrix-MMA library whose
API is compatible with NVIDIA's `nvcuda::wmma`, supporting both CDNA and RDNA. It
lets the same fragment-based source target Matrix Cores on CDNA and WMMA on RDNA.
[VENDOR]

```cpp
#include <rocwmma/rocwmma.hpp>
using namespace rocwmma;
// nvcuda::wmma-style fragment / load / mma_sync / store API
```

**gfx1151 build caveat.** rocWMMA's documented RDNA-with-AI-acceleration targets
are `gfx1100`/`gfx1101`/`gfx1102` (RDNA3 discrete); `gfx1151` (RDNA3.5) support is
**recent** (built with the gfx1151 target on recent ROCm). On older ROCm you may
need to **build rocWMMA from source** against a recent toolchain, passing the
`gfx1151` target via CMake; a full build wants several GB of system memory. Treat
the "build from source on gfx1151" step as a practical hedge, not a hard rule —
check your ROCm version's target list first. [INFERRED]

## Caveats and When WMMA Actually Helps

### No FP8, no sparsity on RDNA3/3.5

**RDNA3/RDNA3.5 WMMA does NOT support FP8/BF8 and has NO structured sparsity.**
Those features arrive with **RDNA4 (`gfx120x`)**, which carries WMMA forward from
RDNA3 and adds 8-bit floating-point formats plus 4:2 structured-sparsity hardware.
[VENDOR] If your kernel needs FP8 matrix math, RDNA3.5 is not an option — you must
use bf16/f16 or the integer (iu8/iu4) paths, or target RDNA4. (RDNA4 also brings
higher per-CU WMMA rates, but those are RDNA4 figures and are not applicable to
gfx1151.)

### WMMA is compute-bound help — little at decode (n=1)

WMMA accelerates **compute-bound** matrix work: large GEMM, prefill, and batched
matmul where arithmetic intensity is high. At **decode with n=1** the dominant
matmuls are quantized GEMV that are **bandwidth-bound** on a shared-DDR5 APU, so a
matrix engine has little to bite on — the bottleneck is memory traffic, not ALU
throughput. See [[opt-rdna-apu-moe-matmul]] for the MoE-matmul case on this part,
and [[arch-rdna35-apu]] for why the APU is bandwidth-bound.

This was observed directly: on gfx1151, llama.cpp's WMMA flash-attention kernel
was measured **2–4× slower** than the non-WMMA TILE kernel for `head_dim=256`,
reaching only **0.22–0.33×** of TILE at decode (`nb=1`); the WMMA path is
correctly disabled there. [IN-HOUSE-MEASURED] —
`AKW-Exp/exp-amd-395/20260609-200325/kernel-profile.md`. (This is about whether to
*use* WMMA for a memory-bound kernel, not a limitation of the ISA itself.)
Separately, llama.cpp sets `AMD_WMMA_AVAILABLE` true for the RDNA3 family
(including RDNA3.5) to trigger stream-K scheduling, even though that particular FA
kernel body uses scalar `half2` MAD rather than WMMA intrinsics.
[IN-HOUSE-MEASURED] — `AKW-Exp/exp-amd-395/20260612-111316/kernel-profile.md`

### CU count

When sizing the part, the full **Ryzen AI Max+ 395 / Radeon 8060S has 40 RDNA3.5
CUs** (`gfx1151`). [VENDOR] The `exp-amd-395` sessions repeatedly record their
GPU as a **20-CU** config — treat that as the documented *session* configuration
(likely a half-enabled/detection sub-config), **not** the part's spec. Any peak
WMMA/FLOPS estimate derived from the 20-CU number is an in-house estimate that
understates the full 40-CU part.

## See Also

- [[arch-rdna35-apu]] — the gfx1151 APU this engine lives in (bandwidth-bound)
- [[arch-amd-gpu-families]] — the RDNA-vs-CDNA family map
- [[arch-cdna3-matrix-core]] / [[arch-cdna4-matrix-core]] — the CDNA MFMA contrast
- [[opt-rdna-apu-moe-matmul]] — where matmul (not attention) dominates decode
- [[opt-hip-vs-cuda-gotchas]] — wave32 and layout footguns when porting from CUDA

## References

- [GPUOpen — How to accelerate AI applications on RDNA 3 using WMMA](https://gpuopen.com/learn/wmma_on_rdna3/)
- [GPUOpen — WMMA guide for AMD RDNA 4 GPUs, part 1](https://gpuopen.com/learn/wmma-guide-amd-rdna-4-gpus-part-1/)
- [GPUOpen — WMMA guide for AMD RDNA 4 GPUs, part 2](https://gpuopen.com/learn/wmma-guide-amd-rdna-4-gpus-part-2/)
- [Chips and Cheese — Examining AMD's RDNA 4 changes in LLVM](https://chipsandcheese.com/p/examining-amds-rdna-4-changes-in-llvm)
- [LLVM clang — WMMA builtins patch](https://www.mail-archive.com/cfe-commits@lists.llvm.org/msg287154.html)
- [ROCm — What is rocWMMA?](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-6.2.4/what-is-rocwmma.html)
- [ROCm — Changelog](https://rocm.docs.amd.com/en/latest/release/changelog.html)
- [rocWMMA on GitHub](https://github.com/ROCm/rocWMMA)
- [VideoCardz — AMD adds WMMA support to GFX11/RDNA3](https://videocardz.com/newz/amd-adds-wmma-wave-matrix-multiply-accumulate-support-to-gfx11-rdna3-architecture-amds-tensor-core)
- `AKW-Exp/exp-amd-395/20260609-200325/kernel-profile.md` — WMMA-vs-TILE FA measurement
- `AKW-Exp/exp-amd-395/20260612-143745/kernel-profile.md` — "RDNA3.5 has no MFMA; ... only WMMA for matrix ops"
- `AKW-Exp/exp-amd-395/20260612-111316/kernel-profile.md` — `AMD_WMMA_AVAILABLE` dispatch note
