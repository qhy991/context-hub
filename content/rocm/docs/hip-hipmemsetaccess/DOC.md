---
name: hip-hipmemsetaccess
description: "Set the access flags for each location specified in desc for the given virtual address range."
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

# hipMemSetAccess

Set the access flags for each location specified in desc for the given virtual address range.

## Signature

```c
hipError_t hipMemSetAccess(void *ptr, size_t size , const hipMemAccessDesc * desc , size_t count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `ptr` | - starting address of the virtual address range. |
| [in] | `size` | - size of the range. |
| [in] | `desc` | - array of hipMemAccessDesc . |
| [in] | `count` | - number of hipMemAccessDesc in desc. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga42ecac69e5ed389aaf287522d1a61305)
