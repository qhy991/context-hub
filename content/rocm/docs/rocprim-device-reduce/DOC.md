---
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
