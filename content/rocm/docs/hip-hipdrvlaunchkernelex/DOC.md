---
name: hip-hipdrvlaunchkernelex
description: "Launches a HIP kernel using the driver API with the specified configuration."
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

# hipDrvLaunchKernelEx

Launches a HIP kernel using the driver API with the specified configuration.

## Signature

```c
hipError_t hipDrvLaunchKernelEx(const HIP_LAUNCH_CONFIG *config, hipFunction_t f, void **params, void **extra);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `config` | Pointer to the kernel launch configuration structure. |
| [in] | `f` | HIP function object representing the device kernel to be launched. |
| [in] | `params` | Array of pointers to the kernel parameters. |
| [in] | `extra` | Array of pointers for additional launch parameters or extra configuration data. |

## Returns

hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

## Notes

- This function dispatches the device kernel represented by a HIP function object. It passes both the kernel parameters and any extra configuration arguments to the kernel launch.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga8f44c3147df2b58c8c5b8d5802674df5)
