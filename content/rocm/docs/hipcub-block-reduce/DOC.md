---
name: hipcub-block-reduce
description: Block-wide reduction utility in hipCUB
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,hipcub,reduce,block
---

# hipcub::BlockReduce

A stateful abstraction for performing block-wide reduction operations across threads in a HIP thread block.

## Syntax

```cpp
template <
    typename T,
    int BLOCK_DIM_X,
    hipcub::BlockReduceAlgorithm ALGORITHM = hipcub::BLOCK_REDUCE_WARP_REDUCTIONS,
    int BLOCK_DIM_Y = 1,
    int BLOCK_DIM_Z = 1>
class BlockReduce;
```

## Description

Equivalent to `cub::BlockReduce` in CUDA. Allows all threads in a block to cooperatively reduce a set of values (e.g., sum, max) to a single value.

## Example

```cpp
#include <hipcub/hipcub.hpp>

__global__ void BlockSumKernel(int* d_in, int* d_out) {
    // Specialize BlockReduce for a 1D block of 128 threads
    typedef hipcub::BlockReduce<int, 128> BlockReduceT;

    // Allocate shared memory for BlockReduce
    __shared__ typename BlockReduceT::TempStorage temp_storage;

    // Obtain a segment of consecutive items that are blocked across threads
    int thread_data = d_in[threadIdx.x];

    // Compute the block-wide sum for thread0
    int aggregate = BlockReduceT(temp_storage).Sum(thread_data);

    if (threadIdx.x == 0) {
        d_out[blockIdx.x] = aggregate;
    }
}
```
