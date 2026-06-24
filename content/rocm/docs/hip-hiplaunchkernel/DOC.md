---
name: hip-hiplaunchkernel
description: "C compliant kernel launch API."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,launch-api
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Launch API
---

# hipLaunchKernel

C compliant kernel launch API.

## Signature

```c
hipError_t hipLaunchKernel(const void *function_address, dim3 numBlocks, dim3 dimBlocks, void **args, size_t sharedMemBytes, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `function_address` | - Kernel stub function pointer. |
| [in] | `numBlocks` | - Number of blocks. |
| [in] | `dimBlocks` | - Dimension of a block |
| [in] | `args` | - Pointer of arguments passed to the kernel. If the kernel has multiple parameters, 'args' should be array of pointers, each points the corresponding argument. |
| [in] | `sharedMemBytes` | - Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `stream` | - Stream where the kernel should be dispatched. May be 0, in which case th default stream is used with associated synchronization rules. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#ga4421a399434f41a1679a84fec3685829)

## Semantics
Enqueues a kernel for execution on the GPU. Configures the hardware packet (e.g., AQL packet in HSA) containing the grid/block dimensions, shared memory size, and arguments, dispatching it to the command processor (CP).

## Example
```cpp
#include <hip/hip_runtime.h>

__global__ void my_kernel(float* a) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    a[idx] *= 2.0f;
}

void run_kernel(float* d_a) {
    void* args[] = { &d_a };
    hipLaunchKernel((const void*)my_kernel, dim3(10), dim3(256), args, 0, nullptr);
}
```
