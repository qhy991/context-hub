---
name: metal-simdgroup-matrix-amx-playbook
description: "Apple AMX coprocessor utilization via simdgroup_matrix instructions: block layouts, fast math, and FlashAttention core primitives."
metadata:
  languages: "cpp"
  versions: "4.0"
  revision: 1
  updated-on: "2026-03-22"
  source: official
  tags: "apple,metal,simdgroup-matrix,amx,mma,tensor-core,flash-attention,matmul,simdgroup_load"
---

# Metal SIMD-group Matrix (AMX) Playbook

Use this page to leverage Apple's underlying AMX (Apple Matrix Coprocessor) hardware for compute-bound operations like GEMM or FlashAttention.

## The AMX Coprocessor

Unlike CUDA, where you write explicit instructions targeting Tensor Cores (e.g., `wgmma` or `mma_sync`), Apple Silicon hides the AMX coprocessor behind the `simdgroup_matrix` abstraction in MSL (Metal Shading Language).

A `simdgroup_matrix` is a 2D block of data distributed across all 32 threads of a SIMD-group (Apple's equivalent of a warp).
Standard sizes:
- Float16: $8 \times 8$ matrix per SIMD-group
- Float32: $8 \times 8$ matrix per SIMD-group

## Core Pipeline

To execute a high-performance tiled GEMM ($D = A \times B + C$), you must:

1. **Load:** Use `simdgroup_load` to fetch a block of data from `threadgroup` (shared) memory or `device` (global) memory directly into a `simdgroup_matrix`.
2. **Multiply-Add:** Use `simdgroup_multiply_accumulate` or `simdgroup_multiply` to perform the matrix math natively on the AMX.
3. **Store:** Use `simdgroup_store` to write the accumulator matrix back to memory.

```cpp
#include <metal_stdlib>
using namespace metal;

// Example AMX Accumulation loop
simdgroup_float8x8 acc;
// Initialize acc dynamically or conventionally
for (int k = 0; k < K_ITER; ++k) {
    simdgroup_float8x8 a_mat;
    simdgroup_float8x8 b_mat;
    simdgroup_load(a_mat, a_ptr + k, elements_per_row);
    simdgroup_load(b_mat, b_ptr + k, elements_per_row);
    simdgroup_multiply_accumulate(acc, a_mat, b_mat, acc);
}
```

## FlashAttention on Metal

For FlashAttention on Apple Silicon, you cannot rely entirely on large `threadgroup` memory like on an NVIDIA H100 (which has up to 228KB of shared memory per SM). 
Apple Silicon GPUs have less `threadgroup` memory per Core (typically ~32KB).

**Pattern:**
- Maximize the use of `simdgroup_matrix` registers to hold the $S$ and $P$ blocks during the Online Softmax calculation.
- Use `simdgroup_max` and SIMD-group reduction primitives (`simd_max`, `simd_sum`) to compute the denominator avoiding round-trips to `threadgroup` memory.

## Strides and Memory Layout

The hardware is highly sensitive to the stride `elements_per_row` argument during `simdgroup_load`.
- For optimal load throughput, the source data should ideally be contiguous (stride equals column width).
- Loading a transposed matrix (e.g., $K^T$) requires explicitly specifying `transpose_matrix` during the `simdgroup_load` call.

## Related Topics

- Metal SIMD-group patterns: `../metal-simdgroup-patterns/DOC.md`
- Metal Tiled Matmul: `../metal-tiled-matmul-patterns/DOC.md`

## Official Source Links (Fact Check)

- Metal Shading Language Spec (simdgroup_matrix): https://developer.apple.com/metal/resources/
- Accelerating Machine Learning with Metal: https://developer.apple.com/documentation/metal/machine_learning

Last cross-check date: 2026-03-22
