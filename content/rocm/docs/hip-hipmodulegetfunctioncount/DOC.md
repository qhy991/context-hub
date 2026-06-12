---
name: hip-hipmodulegetfunctioncount
description: "Returns the number of functions within a module."
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

# hipModuleGetFunctionCount

Returns the number of functions within a module.

## Signature

```c
hipError_t hipModuleGetFunctionCount(unsigned int *count, hipModule_t mod);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `mod` | Module to get function count from |
| [out] | `count` | function count from module |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidContext , hipErrorNotInitialized , hipErrorNotFound ,

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga309efccad8ae2a17c8fb7454707904b7)
