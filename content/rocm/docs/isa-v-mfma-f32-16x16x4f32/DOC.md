---
name: isa-v-mfma-f32-16x16x4f32
description: "Matrix Fused Multiply-Add: 16x16x4 F32 input, F32 accumulation. Higher compute density variant for single-precision GEMM tiling."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,mfma,isa,matrix-core,compute,gemm,cdna
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
---

# v_mfma_f32_16x16x4f32

Matrix Fused Multiply-Accumulate: computes a 16x4 * 4x16 = 16x16 F32 matrix multiply-accumulate.

## Syntax

```asm
v_mfma_f32_16x16x4f32 v[0:15], v[0:3], v[4:7], v[0:15]
```

## Operands

| Operand | Type | Description |
|---------|------|-------------|
| v[dst:dst+15] | VGPR | 16x16 F32 accumulator (16 consecutive VGPRs) |
| srcA | 4 VGPRs | 16x4 F32 input matrix A |
| srcB | 4 VGPRs | 4x16 F32 input matrix B |
| v[src:src+15] | VGPR | Previous accumulator (16 consecutive VGPRs) |

## Description

Computes `D += A * B` where A is 16x4, B is 4x16, producing a 16x16 F32 result.

4x higher compute density than `v_mfma_f32_16x16x1f32` — the preferred building block for tiled FP32 GEMM kernels.

## Architecture Support

| Architecture | GFX | Support |
|-------------|-----|---------|
| CDNA1 | gfx908 | ✓ |
| CDNA2 | gfx90a | ✓ |
| CDNA3 | gfx940/gfx942 | ✓ |
| CDNA4 | gfx950 | ✓ |

## Throughput

| Architecture | Ops/cycle/CU | FLOPs/cycle/CU |
|-------------|-------------|----------------|
| CDNA1 (MI100) | 1 | 2048 |
| CDNA2 (MI250) | 1 | 2048 |
| CDNA3 (MI300X) | 2 | 4096 |
| CDNA4 (MI350X) | 2 | 4096 |

## HIP Intrinsic

```c
#include <rocwmma/rocwmma.h>

rocwmma::fragment<rocwmma::matrix_a, 16, 16, 4, float, rocwmma::row_major> a_frag;
rocwmma::fragment<rocwmma::matrix_b, 16, 16, 4, float, rocwmma::col_major> b_frag;
rocwmma::fragment<rocwmma::accumulator, 16, 16, 4, float> c_frag;
rocwmma::mma_sync(c_frag, a_frag, b_frag, c_frag);
```

## See Also

- `v_mfma_f32_16x16x1f32` — Lower density variant
- `v_mfma_f32_32x32x2f32` — 32x32 tiling variant
- `v_mfma_f32_16x16x16f16` — FP16 input variant

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
