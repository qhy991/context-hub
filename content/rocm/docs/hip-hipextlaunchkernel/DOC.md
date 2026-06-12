---
name: hip-hipextlaunchkernel
description: "Launches kernel from the pointer address, with arguments and shared memory on stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,execution-control
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Execution Control
---

# hipExtLaunchKernel

Launches kernel from the pointer address, with arguments and shared memory on stream.

## Signature

```c
hipError_t hipExtLaunchKernel(const void *function_address, dim3 numBlocks, dim3 dimBlocks, void **args, size_t sharedMemBytes, hipStream_t stream, hipEvent_t startEvent, hipEvent_t stopEvent, int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `function_address` | pointer to the Kernel to launch. |
| [in] | `numBlocks` | number of blocks. |
| [in] | `dimBlocks` | dimension of a block. |
| [in] | `args` | pointer to kernel arguments. |
| [in] | `sharedMemBytes` | Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `stream` | Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules. |
| [in] | `startEvent` | If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API. |
| [in] | `stopEvent` | If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API. |
| [in] | `flags` | The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order. |

## Returns

hipSuccess , hipInvalidDeviceId , hipErrorNotInitialized , hipErrorInvalidValue .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga601d372753e668aba188e2466c414bbd)
