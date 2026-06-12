---
name: hip-hipextlaunchkernelggl
description: "Launches kernel with dimention parameters and shared memory on stream with templated kernel and arguments."
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

# hipExtLaunchKernelGGL

Launches kernel with dimention parameters and shared memory on stream with templated kernel and arguments.

## Signature

```c
hipError_t hipExtLaunchKernelGGL(F kernel, const dim3 &amp;numBlocks, const dim3 &amp;dimBlocks, std::uint32_t sharedMemBytes, hipStream_t stream, hipEvent_t startEvent, hipEvent_t stopEvent, std::uint32_t flags, Args... args);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `kernel` | Kernel to launch. |
| [in] | `numBlocks` | const number of blocks. |
| [in] | `dimBlocks` | const dimension of a block. |
| [in] | `sharedMemBytes` | Amount of dynamic shared memory to allocate for this kernel. HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `stream` | Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules. |
| [in] | `startEvent` | If non-null, specified event will be updated to track the start time of the kernel launch. The event must be created before calling this API. |
| [in] | `stopEvent` | If non-null, specified event will be updated to track the stop time of the kernel launch. The event must be created before calling this API. |
| [in] | `flags` | The value of hipExtAnyOrderLaunch, signifies if kernel can be launched in any order. |
| [in] | `args` | templated kernel arguments. |

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga82a15dac5d1205c69c20d84245078bf6)
