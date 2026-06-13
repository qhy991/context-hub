---
name: hip-hiplaunchkernelexc
description: "Launches a HIP kernel using a generic function pointer and the specified configuration."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Execution Control
---

# hipLaunchKernelExC

Launches a HIP kernel using a generic function pointer and the specified configuration.

## Signature

```c
hipError_t hipLaunchKernelExC(const hipLaunchConfig_t *config, const void *fPtr, void **args);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `config` | Pointer to the kernel launch configuration structure. |
| [in] | `fPtr` | Pointer to the device kernel function. |
| [in] | `args` | Array of pointers to the kernel arguments. |

## Returns

hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

## Notes

- This function is equivalent to hipLaunchKernelEx but accepts the kernel as a generic function pointer.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga20d5257a68cc6c80c06745f001b0c218)
