---
name: hip-hippointergetattribute
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

# hipPointerGetAttribute

Returns information about the specified pointer.[BETA].

## Signature

```c
hipError_t hipPointerGetAttribute(void *data, hipPointer_attribute attribute, hipDeviceptr_t ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `data` | Returned pointer attribute value |
| [in] | `attribute` | Attribute to query for |
| [in] | `ptr` | Pointer to get attributes for |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaf147601f5094423a9810db112ef8ef07)
