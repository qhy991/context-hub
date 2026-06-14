import os

ascendc_matmul_advanced_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/ascendc/docs/ascendc-matmul-advanced"
rocprim_block_reduce_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/docs/rocprim-block-reduce"
rocprim_device_reduce_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/docs/rocprim-device-reduce"

ascendc_matmul_advanced_doc = """---
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
"""

rocprim_block_reduce_doc = """---
name: rocprim-block-reduce
description: rocPRIM Block Reduction primitive
metadata:
  languages: hip-cpp
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,hip,rocprim,reduction,block-level,lds
---

# rocPRIM Block Reduce

`rocprim::block_reduce` is a high-level primitive for performing a reduction operation across all threads in a HIP Thread Block.

## Description

Under the hood, `block_reduce` abstracts away the complexity of Wavefront DPP instructions and LDS (Local Data Share) synchronization. It guarantees high performance while handling bank conflict avoidance automatically.

## Syntax

```cpp
#include <rocprim/rocprim.hpp>

template<
    typename T,
    unsigned int BlockSize,
    rocprim::block_reduce_algorithm Algorithm = rocprim::block_reduce_algorithm::using_warp_reduce
>
class block_reduce {
public:
    // Shared memory (LDS) required by the algorithm
    struct storage_type { ... };

    // Performs reduction, returning result only to thread 0
    template<typename BinaryFunction>
    __device__ void reduce(T input, T& output, storage_type& storage, BinaryFunction reduce_op);
};
```

## Example Usage

```cpp
__global__ void block_reduce_kernel(float* d_input, float* d_output) {
    const unsigned int block_size = 256;
    const unsigned int tid = threadIdx.x;
    
    // Allocate LDS memory required by rocPRIM
    __shared__ rocprim::block_reduce<float, block_size>::storage_type storage;
    
    float input_val = d_input[blockIdx.x * block_size + tid];
    float output_val;
    
    // Perform block-wide sum reduction
    rocprim::block_reduce<float, block_size> reducer;
    reducer.reduce(input_val, output_val, storage, rocprim::plus<float>());
    
    // Only thread 0 has the valid result
    if (tid == 0) {
        d_output[blockIdx.x] = output_val;
    }
}
```

## Algorithms
- `using_warp_reduce`: Uses hardware wavefront shuffles (DPP) before using LDS for cross-wave reduction. This is the default and fastest method.
"""

rocprim_device_reduce_doc = """---
name: rocprim-device-reduce
description: rocPRIM Device Reduction primitive
metadata:
  languages: hip-cpp
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,hip,rocprim,reduction,device-level,global-memory
---

# rocPRIM Device Reduce

`rocprim::device_reduce` is a host-side API that performs a grid-level reduction over data stored in Global Memory, writing the single accumulated result back to Global Memory (or host memory).

## Description

Grid-level reductions require synchronizing across multiple Thread Blocks. Because HIP does not have a global barrier, `device_reduce` typically launches a multi-pass kernel (or uses atomics).

## Syntax

```cpp
#include <rocprim/rocprim.hpp>

template<
    typename InputIterator,
    typename OutputIterator,
    typename InitialValueType,
    typename BinaryFunction
>
hipError_t device_reduce(
    void * temporary_storage,
    size_t & storage_size,
    InputIterator input,
    OutputIterator output,
    InitialValueType initial_value,
    size_t size,
    BinaryFunction reduce_op,
    hipStream_t stream = 0
);
```

## The Workspace (Two-Pass) Pattern

A defining characteristic of rocPRIM (and cub) device algorithms is the two-pass execution model for handling `temporary_storage`.

1. **Size Query Pass**: Call the function with `temporary_storage = nullptr`. It calculates and returns the required bytes in `storage_size`.
2. **Allocation**: Use `hipMalloc` to allocate `storage_size` bytes.
3. **Execution Pass**: Call the function again, passing the allocated pointer.

## Example Usage

```cpp
size_t size = 1000000;
float* d_input;
float* d_output;
// ... (initialize pointers)

// 1. Query required workspace size
void* d_temp_storage = nullptr;
size_t temp_storage_size_bytes = 0;

rocprim::device_reduce(
    d_temp_storage, temp_storage_size_bytes,
    d_input, d_output,
    0.0f, size, rocprim::plus<float>()
);

// 2. Allocate workspace
hipMalloc(&d_temp_storage, temp_storage_size_bytes);

// 3. Perform reduction
rocprim::device_reduce(
    d_temp_storage, temp_storage_size_bytes,
    d_input, d_output,
    0.0f, size, rocprim::plus<float>()
);

// 4. Free workspace
hipFree(d_temp_storage);
```
"""

os.makedirs(ascendc_matmul_advanced_path, exist_ok=True)
os.makedirs(rocprim_block_reduce_path, exist_ok=True)
os.makedirs(rocprim_device_reduce_path, exist_ok=True)

with open(os.path.join(ascendc_matmul_advanced_path, "DOC.md"), "w") as f:
    f.write(ascendc_matmul_advanced_doc)

with open(os.path.join(rocprim_block_reduce_path, "DOC.md"), "w") as f:
    f.write(rocprim_block_reduce_doc)

with open(os.path.join(rocprim_device_reduce_path, "DOC.md"), "w") as f:
    f.write(rocprim_device_reduce_doc)

print("Context Hub generation script complete.")
