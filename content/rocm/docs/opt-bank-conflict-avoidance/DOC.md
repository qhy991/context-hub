---
name: opt-bank-conflict-avoidance
description: "Optimization guide: Avoiding LDS bank conflicts on AMD CDNA GPUs. Critical for achieving high memory throughput in GEMM, attention, and reduction kernels."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,optimization,lds,bank-conflict,memory,cdna
  isa_category: optimization
  instruction_type: guide
  hw_unit: lds
---

# Avoiding LDS Bank Conflicts on AMD CDNA GPUs

Comprehensive guide to understanding and avoiding bank conflicts in LDS (Local Data Share) on AMD CDNA architectures.

## Background: LDS Architecture

| Property | CDNA1-3 | CDNA4 |
|----------|---------|-------|
| LDS per CU | 64 KB | 64 KB |
| Banks | 32 | 32 |
| Bank width | 4 bytes (dword) | 4 bytes (dword) |
| Reads/cycle/CU | 2 | 2 |
| Writes/cycle/CU | 2 | 2 |

> **Note**: AMD LDS has 32 banks, unlike CUDA shared memory which also has 32 banks. However, AMD wavefront is 64 threads (vs CUDA warp of 32), so bank conflicts manifest differently.

## What Are Bank Conflicts?

When two or more threads in the same wavefront access different addresses **in the same LDS bank** during the same cycle, the accesses are serialized.

```
Bank conflict example (BAD):
Thread  0 → address 0   (bank 0)
Thread  1 → address 4   (bank 1)  ← bank 1
Thread 16 → address 64  (bank 0)  ← CONFLICT with thread 0!
Thread 17 → address 68  (bank 1)  ← CONFLICT with thread 1!
```

Each additional conflict adds ~4 cycles latency.

## Techniques

### 1. Padding (Most Common)

Add 1 dword of padding per row to shift bank assignments:

```c
// BAD: 64 columns → threads 0 and 16 always conflict
__shared__ float tile[64][64];

// GOOD: 65 columns → bank conflict eliminated
__shared__ float tile[64][65];

// Access pattern unchanged:
float val = tile[row][col];  // no code change needed
```

**Padding formula**: `padded_width = original_width + (original_width % banks == 0 ? 1 : 0)`

### 2. Swizzled Access Patterns

Reorder data in LDS using XOR swizzling:

```c
__device__ uint32_t lds_swizzle(uint32_t addr) {
    uint32_t row = addr >> 5;      // divide by 32 (bank count)
    uint32_t col = addr & 0x1F;    // bank index
    return (row ^ col) * 4;        // swizzled address
}
```

### 3. Vectorized Reads

Use wider loads to reduce the number of LDS transactions:

```c
// Instead of 4 float reads (4 LDS ops):
float a = tile[r][c];
float b = tile[r][c+1];
float c = tile[r][c+2];
float d = tile[r][c+3];

// Use float4 read (1 LDS op, 128-bit):
float4 abcd = *((float4*)&tile[r][c]);
```

### 4. Read2 Instructions

Use `ds_read2_b64` or `ds_read2st64_b64` to read two values in one instruction:

```c
// Compiler hint for paired reads
float2 vals = *((float2*)&tile[r][c]);
```

### 5. Column-Major for MFMA

MFMA instructions expect column-major data in certain layouts. Store transposed to avoid runtime transpose:

```c
// When feeding MFMA, store in the layout it expects
// CDNA MFMA: srcA row-major, srcB column-major (for standard GEMM)
// Adjust your LDS tile layout accordingly
```

## Diagnosis Tools

```bash
# Profile LDS bank conflicts
rocprof-compute --hsa-stats ./your_kernel

# Check LDS utilization
rocprofv3 --stats ./your_kernel
```

## Quick Reference: Conflict-Free Access Patterns

| Pattern | Stride (dwords) | Conflict? |
|---------|-----------------|-----------|
| Sequential | 1 | ✅ No conflict |
| Stride 2 | 2 | ✅ No conflict |
| Stride 4 | 4 | ✅ No conflict |
| Stride 8 | 8 | ✅ No conflict |
| Stride 16 | 16 | ✅ No conflict |
| Stride 32 | 32 | ❌ 2-way conflict |
| Stride 64 | 64 | ❌ 2-way conflict |
| Stride 33 | 33 | ✅ No conflict (padded!) |

## See Also

- `isa-ds-read2st64-b64` — Paired LDS read instruction
- [AMDGPU Kernel Optimization Guide](https://github.com/nod-ai/shark-ai/blob/main/docs/amdgpu_kernel_optimization_guide.md)
- [MI300X Workload Optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html)

## References

- [CDNA4 Architecture Whitepaper](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-4-architecture-whitepaper.pdf)
- [Matrix Core Programming CDNA3/CDNA4](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)
