---
name: hip-hipmodulelaunchkernel
description: "launches kernel f with launch parameters and shared memory on stream with arguments passed to kernelparams or extra"
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

# hipModuleLaunchKernel

launches kernel f with launch parameters and shared memory on stream with arguments passed to kernelparams or extra

## Signature

```c
hipError_t hipModuleLaunchKernel(hipFunction_t f, unsigned int gridDimX, unsigned int gridDimY, unsigned int gridDimZ, unsigned int blockDimX, unsigned int blockDimY, unsigned int blockDimZ, unsigned int sharedMemBytes, hipStream_t stream, void **kernelParams, void **extra);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `f` | Kernel to launch. |
| [in] | `gridDimX` | X grid dimension specified as multiple of blockDimX. |
| [in] | `gridDimY` | Y grid dimension specified as multiple of blockDimY. |
| [in] | `gridDimZ` | Z grid dimension specified as multiple of blockDimZ. |
| [in] | `blockDimX` | X block dimensions specified in work-items |
| [in] | `blockDimY` | Y grid dimension specified in work-items |
| [in] | `blockDimZ` | Z grid dimension specified in work-items |
| [in] | `sharedMemBytes` | Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `stream` | Stream where the kernel should be dispatched. May be 0, in which case th default stream is used with associated synchronization rules. |
| [in] | `kernelParams` | Kernel parameters to launch |
| [in] | `extra` | Pointer to kernel arguments. These are passed directly to the kernel and must be in the memory layout and alignment expected by the kernel. All passed arguments must be naturally aligned according to their type. The memory address of each argument should be a multiple of its size in bytes. Please refer to hip_porting_driver_api.md for sample usage. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue

## Notes

- Please note, HIP does not support kernel launch with total work items defined in dimension with size gridDim x blockDim &gt;= 2^32. So gridDim.x * blockDim.x, gridDim.y * blockDim.y and gridDim.z * blockDim.z are always less than 2^32.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga2e4de5937aa8171e9eda16c881ed0674)
