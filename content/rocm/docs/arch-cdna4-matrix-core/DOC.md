---
name: arch-cdna4-matrix-core
description: "CDNA4 (gfx950 / MI350X) matrix core capabilities: dual CMA, scaled MFMA, FP8/FP6/FP4, and LDS transpose."
metadata:
  languages: hip
  architectures: cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,architecture,cdna4,matrix-core,mfma,scaled-mfma
  isa_category: architecture
  instruction_type: guide
  hw_unit: matrix-core
---

# CDNA4 Matrix Core Architecture

Hardware overview for MI350X/MI355X (gfx950) matrix acceleration.

## Compute Organization

| Property | CDNA4 |
|----------|-------|
| GFX ID | gfx950 |
| CMA per CU | 2 (dual matrix pipes) |
| Wavefront size | 64 |
| LDS per CU | 64 KB |
| Scaled MFMA | Yes (block-scaled F8/F6/F4) |
| LDS transpose reads | Yes |

## Key ISA Families

- Standard MFMA: `v_mfma_f32_*`, `v_mfma_i32_*`
- FP8/BF8 MFMA: `v_mfma_f32_*_fp8_*`, `v_mfma_f32_*_bf8_*`
- Scaled MFMA (CDNA4): `v_mfma_scale_f32_*`
- Low-precision FP4/FP6 paths for inference-scale GEMM

## Programming Paths

1. **Composable Kernel / CK Tile** — recommended for GEMM, attention, MoE
2. **rocWMMA** — portable matrix API (CUDA WMMA-like)
3. **Inline MFMA asm** — maximum control for fused kernels

## Related context-hub Entries

- Search: `chub search "mfma scale"`
- ISA examples: `isa-v-mfma-scale-f32-16x16x128-f8f6f4`

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
- [Matrix Core Programming on CDNA](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)
