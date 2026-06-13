---
name: hip-hipmoduleloaddataex
description: "builds module from code object which resides in host memory. Image is pointer to that location. Options are not used. hipModuleLoadData is called."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Module Management
---

# hipModuleLoadDataEx

builds module from code object which resides in host memory. Image is pointer to that location. Options are not used. hipModuleLoadData is called.

## Signature

```c
hipError_t hipModuleLoadDataEx(hipModule_t *module, const void *image, unsigned int numOptions, hipJitOption *options, void **optionValues);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `image` | The pointer to the location of data |
| [out] | `module` | Retuned module |
| [in] | `numOptions` | Number of options |
| [in] | `options` | Options for JIT |
| [in] | `optionValues` | Option values for JIT |

## Returns

hipSuccess, hipErrorNotInitialized, hipErrorOutOfMemory, hipErrorNotInitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga3e70722338894f48540c7be9a136af79)
