---
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
