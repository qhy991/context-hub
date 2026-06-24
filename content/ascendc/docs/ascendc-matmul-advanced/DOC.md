---
name: ascendc-matmul-advanced
description: Advanced tiling and iteration APIs for Matmul
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,cube,matmul,tiling,iterate
---

# Matmul Advanced APIs

For matrices that exceed the capacity of the L1 or Unified Buffer (UB), the `Matmul` class provides advanced iteration and tiling controls. This allows developers to manually load blocks, compute them, and handle edge cases (tail blocks).

## Semantics

```cpp
// Advanced Matmul execution flow:
matmul_obj.SetTensorA(A);
matmul_obj.SetTensorB(B);
matmul_obj.SetBias(bias);
matmul_obj.IterateAll(C);
// Computes C = A * B + bias iteratively block-by-block.
```

## Hardware Unit

Cube Unit

## Advanced Tiling APIs

### 1. `SetSubBlockIdx` / `SetTail`
Used to manage the current coordinates in the global matrix and handle dimensions that are not exact multiples of the `BLOCK_SIZE`.

```cpp
// Set the coordinates of the current sub-block being processed
matmul.SetSubBlockIdx(subBlockIdx_M, subBlockIdx_N, subBlockIdx_K);

// Define the exact sizes of the tail if dimensions aren't aligned to 16
matmul.SetTail(tail_M, tail_N, tail_K);
```

### 2. Iteration Control
Instead of a single `Launch()`, complex loops use `IterateAll()` or manual `Iterate()` to control the `M-N-K` loop progression.

```cpp
template <typename T>
class Matmul {
public:
    // Automatically iterates through all sub-blocks
    bool IterateAll(LocalTensor<T>& a, LocalTensor<T>& b, LocalTensor<T>& c);
    
    // Manually advance the computation by one block
    void Iterate();
    
    // Retrieve the computed partial/final block
    template <typename U>
    void GetTensorC(LocalTensor<U>& c);
};
```

## Tiling Modes

- **`REG_TILING`**: Tiling parameters are passed via registers at runtime (more flexible for dynamic shapes).
- **`SYS_TILING`**: Tiling parameters are pre-compiled and fetched from global memory (lower instruction overhead for static shapes).

## Example: Manual Iteration with Double Buffering

```cpp
using namespace ascendc;

Matmul<float16> matmul;
matmul.Init(M, N, K);

// Example configuration for iterating over K dimension
for (int k_idx = 0; k_idx < num_k_blocks; ++k_idx) {
    // 1. CopyIn: Load A and B tiles from GM to L1
    DataCopy(A_l1, A_gm_block, block_size);
    DataCopy(B_l1, B_gm_block, block_size);
    
    // 2. Compute: Push instruction to Cube
    // Iterate() performs the MAC operation and accumulates in L0C
    matmul.Iterate(A_l1, B_l1);
}

// 3. CopyOut: Move final accumulated result from L0C to UB
matmul.GetTensorC(C_ub);
DataCopy(C_gm, C_ub, result_size);
```
