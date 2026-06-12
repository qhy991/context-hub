---
name: opt-mfma-scheduling
description: "Optimization guide: interleaving MFMA with global/LDS memory operations on CDNA GPUs to hide matrix-core latency."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,optimization,mfma,matrix-core,pipeline
  isa_category: optimization
  instruction_type: guide
  hw_unit: matrix-core
---

# MFMA Scheduling on CDNA

Practical guidance for keeping AMD matrix cores fed while hiding memory latency.

## Pipeline Pattern

1. Prefetch next K-tile into LDS (or registers)
2. Issue MFMA batch on current tile
3. Overlap epilogue / reduction with next prefetch

```cpp
for (int k = 0; k < K; k += TILE_K) {
    prefetch_ab(k + TILE_K);
    mfma_accumulate(k);
    __syncthreads();
}
```

## Tile Size Selection

| Goal | Typical MFMA tile | Trade-off |
|------|-------------------|-----------|
| Max throughput | 16×16×16 FP16 | Higher register pressure |
| Occupancy friendly | 4×4×4 / smaller tiles | Lower FLOPs per instruction |
| FP8 inference | 16×16×32 FP8 | CDNA3+ only |

## Tooling

- **CK / CK Tile**: production GEMM/attention pipelines with built-in scheduling
- **rocprof-compute**: inspect `SQ_INSTS_VALU_MFMA` vs memory stall counters
- **Inline asm**: research kernels only — verify register layout per ISA guide

## See Also

- ROCm-KernelWiki-Q: `technique-mfma-scheduling`
- context-hub ISA entries: `isa-v-mfma-*`

## References

- [Matrix Core Programming on CDNA](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)
- [CDNA4 ISA Reference](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
