---
name: hip-hipmemgetallocationgranularity
description: "Calculates either the minimal or recommended granularity."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,virtual-memory-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Virtual Memory Management
---

# hipMemGetAllocationGranularity

Calculates either the minimal or recommended granularity.

## Signature

```c
hipError_t hipMemGetAllocationGranularity(size_t *granularity, const hipMemAllocationProp *prop, hipMemAllocationGranularity_flags option);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `granularity` | - returned granularity. |
| [in] | `prop` | - location properties. |
| [in] | `option` | - determines which granularity to return. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga64aa4fd4fea31e1c0e291cca605c9821)
