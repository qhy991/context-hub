---
name: hip-hipmemcreate
description: "Creates a memory allocation described by the properties and size."
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

# hipMemCreate

Creates a memory allocation described by the properties and size.

## Signature

```c
hipError_t hipMemCreate(hipMemGenericAllocationHandle_t *handle, size_t size , const hipMemAllocationProp *prop, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `handle` | - value of the returned handle. |
| [in] | `size` | - size of the allocation. |
| [in] | `prop` | - properties of the allocation. |
| [in] | `flags` | - currently unused, must be zero. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga906e9c4cc3f6e8bda1116cea1e12bdc5)
