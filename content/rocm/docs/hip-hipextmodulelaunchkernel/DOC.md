---
name: hip-hipextmodulelaunchkernel
description: "Launches kernel with parameters and shared memory on stream with arguments passed to kernel params or extra arguments."
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

# hipExtModuleLaunchKernel

Launches kernel with parameters and shared memory on stream with arguments passed to kernel params or extra arguments.

## Signature

```c
hipError_t hipExtModuleLaunchKernel(hipFunction_t f, uint32_t globalWorkSizeX, uint32_t globalWorkSizeY, uint32_t globalWorkSizeZ, uint32_t localWorkSizeX, uint32_t localWorkSizeY, uint32_t localWorkSizeZ, size_t sharedMemBytes, hipStream_t hStream, void **kernelParams, void **extra, hipEvent_t startEvent, hipEvent_t stopEvent, uint32_t flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `f` | Kernel to launch. |
| [in] | `globalWorkSizeX` | X grid dimension specified in work-items. |
| [in] | `globalWorkSizeY` | Y grid dimension specified in work-items. |
| [in] | `globalWorkSizeZ` | Z grid dimension specified in work-items. |
| [in] | `localWorkSizeX` | X block dimension specified in work-items. |
| [in] | `localWorkSizeY` | Y block dimension specified in work-items. |
| [in] | `localWorkSizeZ` | Z block dimension specified in work-items. |
| [in] | `sharedMemBytes` | Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `hStream` | Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules. |
| [in] | `kernelParams` | pointer to kernel parameters. |
| [in] | `extra` | Pointer to kernel arguments. These are passed directly to the kernel and must be in the memory layout and alignment expected by the kernel. All passed arguments must be naturally aligned according to their type. The memory address of each argument should be a multiple of its size in bytes. Please refer to hip_porting_driver_api.md for sample usage. |
| [in] | `startEvent` | If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API. |
| [in] | `stopEvent` | If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API. |
| [in] | `flags` | The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order. |

## Returns

hipSuccess , hipInvalidDeviceId , hipErrorNotInitialized , hipErrorInvalidValue .

## Notes

- HIP/ROCm actually updates the start event when the associated kernel completes. Currently, timing between startEvent and stopEvent does not include the time it takes to perform a system scope release/cache flush - only the time it takes to issues writes to cache.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga14d4fba7af1cdc9da9949031ebd187d2)
