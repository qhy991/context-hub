---
name: isa-v-mfma-f32-32x32x2f32
description: "Matrix Fused Multiply-Add: 32x32x2 F32 input, F32 accumulation. Large tile variant for higher arithmetic intensity."
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

# v_mfma_f32_32x32x2f32

Matrix Fused Multiply-Accumulate: 32x32x2 tile for higher arithmetic intensity.

## Syntax

```asm
v_mfma_f32_32x32x2f32 v[0:31], v[0:3], v[4:7], v[0:31]
```

## Operands

| Operand | Type | Count | Description |
|---------|------|-------|-------------|
| v[dst:dst+31] | VGPR | 32 | 32x32 F32 accumulator |
| srcA | VGPR | 4 | 32x2 F32 input matrix A |
| srcB | VGPR | 4 | 2x32 F32 input matrix B |
| v[src:src+31] | VGPR | 32 | Previous accumulator |

## Description

Computes `D += A * B` where A is 32x2, B is 2x32, producing a 32x32 F32 result.

Requires 32 VGPRs per accumulator — high register pressure but maximum arithmetic intensity for FP32 workloads.

## Architecture Support

| Architecture | GFX | Support |
|-------------|-----|---------|
| CDNA1 | gfx908 | ✓ |
| CDNA2 | gfx90a | ✓ |
| CDNA3 | gfx940/gfx942 | ✓ |
| CDNA4 | gfx950 | ✓ |

## Register Pressure Considerations

- 32 VGPRs per accumulator tile
- With double buffering: 64 VGPRs just for accumulators
- Limits occupancy: max 8 waves/CU with double-buffered 32x32 tiles
- Consider 16x16 tiles for higher occupancy kernels

## See Also

- `v_mfma_f32_16x16x4f32` — Lower register pressure (16 VGPRs)
- `v_mfma_f32_4x4x1f32` — Minimal variant

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
