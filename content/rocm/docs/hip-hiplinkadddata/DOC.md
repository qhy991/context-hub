---
name: hip-hiplinkadddata
description: "Adds bitcode data to be linked with options."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,module-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Module Management
---

# hipLinkAddData

Adds bitcode data to be linked with options.

## Signature

```c
hipError_t hipLinkAddData(hipLinkState_t state, hipJitInputType type, void *data, size_t size , const char *name, unsigned int numOptions, hipJitOption *options, void **optionValues);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `state` | hip link state |
| [in] | `type` | Type of the input data or bitcode |
| [in] | `data` | Input data which is null terminated |
| [in] | `size` | Size of the input data |
| [in] | `name` | Optional name for this input |
| [in] | `numOptions` | Size of the options |
| [in] | `options` | Array of options applied to this input |
| [in] | `optionValues` | Array of option values cast to void* |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidHandle

## Notes

- If adding the file fails, it will

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gaf3bda16dabe443ea621212c39a0573f2)
