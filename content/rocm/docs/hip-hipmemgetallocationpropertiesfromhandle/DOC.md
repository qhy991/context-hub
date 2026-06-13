---
name: hip-hipmemgetallocationpropertiesfromhandle
description: "Retrieve the property structure of the given handle."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Virtual Memory Management
---

# hipMemGetAllocationPropertiesFromHandle

Retrieve the property structure of the given handle.

## Signature

```c
hipError_t hipMemGetAllocationPropertiesFromHandle(hipMemAllocationProp *prop, hipMemGenericAllocationHandle_t handle);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `prop` | - properties of the given handle. |
| [in] | `handle` | - handle to perform the query on. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#gab4d484e2b8da613694a48738817f4b24)
