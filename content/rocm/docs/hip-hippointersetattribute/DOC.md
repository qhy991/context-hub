---
name: hip-hippointersetattribute
description: "Sets information on the specified pointer.[BETA]."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipPointerSetAttribute

Sets information on the specified pointer.[BETA].

## Signature

```c
hipError_t hipPointerSetAttribute(const void *value, hipPointer_attribute attribute, hipDeviceptr_t ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `value` | Sets pointer attribute value |
| [in] | `attribute` | Attribute to set |
| [in] | `ptr` | Pointer to set attributes for |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad35dd7d821d5a4d32693e3eada647177)
