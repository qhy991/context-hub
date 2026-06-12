---
name: hip-hipdrvpointergetattributes
description: "Returns information about the specified pointer.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Memory Management
---

# hipDrvPointerGetAttributes

Returns information about the specified pointer.[BETA].

## Signature

```c
hipError_t hipDrvPointerGetAttributes(unsigned int numAttributes, hipPointer_attribute *attributes, void **data, hipDeviceptr_t ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `numAttributes` | number of attributes to query for |
| [in] | `attributes` | attributes to query for |
| [in,out] | `data` | a two-dimensional containing pointers to memory locations where the result of each attribute query will be written to |
| [in] | `ptr` | pointer to get attributes for |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad0d11c0ccac6e262c147e5b47642cf1d)
