---
name: isa-v-mfma-f32-16x16x1f32
description: "Matrix Fused Multiply-Add: 16x16x1 F32 input, F32 accumulation. Basic MFMA instruction for single-precision matrix operations."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,mfma,isa,matrix-core,compute,cdna
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
---

# v_mfma_f32_16x16x1f32

Matrix Fused Multiply-Accumulate instruction: multiplies a 16x1 F32 matrix by a 1x16 F32 matrix and accumulates into a 16x16 F32 result.

## Syntax

```asm
v_mfma_f32_16x16x1f32 v[0:15], v0, v1, v[0:15]
```

## Operands

| Operand | Type | Description |
|---------|------|-------------|
| v[dst:dst+15] | VGPR | 16x16 F32 accumulator (16 consecutive VGPRs) |
| srcA | VGPR/SGPR/inline | 16x1 F32 input vector |
| srcB | VGPR/SGPR/inline | 1x16 F32 input vector |
| v[src:src+15] | VGPR | Previous accumulator value (16 consecutive VGPRs) |

## Description

Performs a rank-1 update of a 16x16 F32 matrix: `D += A * B^T` where A is 16x1 and B is 1x16.

This is the most basic MFMA operation, useful for:
- Vector outer products
- Rank-1 matrix updates
- Building blocks for tiled GEMM

## Hardware Unit

Matrix Core (CMA - Compute Matrix Accelerator on CDNA3+)

## Architecture Support

| Architecture | GFX | Support |
|-------------|-----|---------|
| CDNA1 | gfx908 | ✓ |
| CDNA2 | gfx90a | ✓ |
| CDNA3 | gfx940/gfx942 | ✓ |
| CDNA4 | gfx950 | ✓ |

## Throughput

| Architecture | Throughput (per CU per cycle) |
|-------------|-------------------------------|
| CDNA1 (MI100) | 1 per cycle |
| CDNA2 (MI250) | 1 per cycle |
| CDNA3 (MI300X) | 2 per cycle (dual CMA) |
| CDNA4 (MI350X) | 2 per cycle (dual CMA) |

## HIP Intrinsic

```c
#include <rocwmma/rocwmma.h>

// Using rocWMMA
rocwmma::fragment<rocwmma::matrix_a, 16, 16, 1, float, rocwmma::row_major> a_frag;
rocwmma::fragment<rocwmma::matrix_b, 16, 16, 1, float, rocwmma::col_major> b_frag;
rocwmma::fragment<rocwmma::accumulator, 16, 16, 1, float> c_frag;
rocwmma::fill_fragment(c_frag, 0.0f);
rocwmma::load_matrix_sync(a_frag, a_ptr, 16);
rocwmma::load_matrix_sync(b_frag, b_ptr, 1);
rocwmma::mma_sync(c_frag, a_frag, b_frag, c_frag);
```

## See Also

- `v_mfma_f32_16x16x4f32` — 16x16x4 variant (higher compute density)
- `v_mfma_f32_32x32x1f32` — 32x32x1 variant
- [Matrix Core Programming on CDNA3/CDNA4](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
- [AMD Machine-Readable ISA (XML)](https://gpuopen.com/machine-readable-isa/)
