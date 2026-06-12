---
name: hip-hiplinkaddfile
description: "Adds a file with bitcode to be linked with options."
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

# hipLinkAddFile

Adds a file with bitcode to be linked with options.

## Signature

```c
hipError_t hipLinkAddFile(hipLinkState_t state, hipJitInputType type, const char *path, unsigned int numOptions, hipJitOption *options, void **optionValues);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `state` | hip link state |
| [in] | `type` | Type of the input data or bitcode |
| [in] | `path` | Path to the input file where bitcode is present |
| [in] | `numOptions` | Size of the options |
| [in] | `options` | Array of options applied to this input |
| [in] | `optionValues` | Array of option values cast to void* |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- If adding the file fails, it will

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga4060b26dae6d689b859b047649bcc3a4)
