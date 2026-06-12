---
name: hip-hipmoduleloadfatbinary
description: "Loads fatbin object."
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

# hipModuleLoadFatBinary

Loads fatbin object.

## Signature

```c
hipError_t hipModuleLoadFatBinary(hipModule_t *module, const void *fatbin);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `fatbin` | fatbin to be loaded as a module |
| [out] | `module` | Module |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidContext , hipErrorFileNotFound , hipErrorOutOfMemory , hipErrorSharedObjectInitFailed , hipErrorNotInitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gadd464c89066b98fda5c7e0dfe20557e5)
