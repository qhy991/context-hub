---
name: arch-cdna3-matrix-core
description: "CDNA3 (gfx940/gfx942 / MI300X/A) matrix core capabilities: dual CMA, FP8/BF8 MFMA, and high-bandwidth HBM3."
metadata:
  languages: hip
  architectures: cdna3
  versions: 'CDNA3+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,architecture,cdna3,matrix-core,mfma,fp8,mi300x
  isa_category: architecture
  instruction_type: guide
  hw_unit: matrix-core
---

# CDNA3 Matrix Core Architecture

Hardware overview for MI300X/MI300A (gfx940/gfx942).

## Compute Organization

| Property | CDNA3 |
|----------|-------|
| GFX IDs | gfx940, gfx942 |
| CMA per CU | 2 |
| Wavefront size | 64 |
| LDS per CU | 64 KB |
| FP8 MFMA | Yes (FP8/BF8) |
| HBM | 192 GB HBM3 |
| Peak HBM BW | ~5.3 TB/s |

## Kernel-Relevant Notes

- FP8 GEMM/attention kernels should target `v_mfma_f32_*_fp8_*` / `*_bf8_*` families
- Dual CMA enables higher sustained MFMA throughput when pipelines are well interleaved
- CK Tile FMHA is the primary attention path on MI300X

## References

- [CDNA3 ISA Reference](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna3-instruction-set-architecture.pdf)
- [MI300X Workload Optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html)
- [Matrix Core Programming on CDNA](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)
