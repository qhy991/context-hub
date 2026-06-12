---
name: hip-hipmemretainallocationhandle
description: "Returns the allocation handle of the backing memory allocation given the address."
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

# hipMemRetainAllocationHandle

Returns the allocation handle of the backing memory allocation given the address.

## Signature

```c
hipError_t hipMemRetainAllocationHandle(hipMemGenericAllocationHandle_t *handle, void *addr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `handle` | - handle representing addr. |
| [in] | `addr` | - address to look up. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga67a29a33c4e047c4c3663a0695676742)
