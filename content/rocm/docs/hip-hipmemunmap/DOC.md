---
name: hip-hipmemunmap
description: "Unmap memory allocation of a given address range."
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

# hipMemUnmap

Unmap memory allocation of a given address range.

## Signature

```c
hipError_t hipMemUnmap(void *ptr, size_t size);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `ptr` | - starting address of the range to unmap. |
| [in] | `size` | - size of the virtual address range. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga614612815d3f36c73de75ad47b24f110)
