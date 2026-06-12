---
name: hip-hipextlaunchmultikernelmultidevice
description: "Launches kernels on multiple devices and guarantees all specified kernels are dispatched on respective streams before enqueuing any other work on the specified streams from any other threads."
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

# hipExtLaunchMultiKernelMultiDevice

Launches kernels on multiple devices and guarantees all specified kernels are dispatched on respective streams before enqueuing any other work on the specified streams from any other threads.

## Signature

```c
hipError_t hipExtLaunchMultiKernelMultiDevice(hipLaunchParams *launchParamsList, int numDevices, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `launchParamsList` | List of launch parameters, one per device. |
| [in] | `numDevices` | Size of the launchParamsList array. |
| [in] | `flags` | Flags to control launch behavior. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga24070776eacdf32ba3c4f339315df6ff)
