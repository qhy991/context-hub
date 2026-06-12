---
name: hip-hipmemrelease
description: "Release a memory handle representing a memory allocation which was previously allocated through hipMemCreate."
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

# hipMemRelease

Release a memory handle representing a memory allocation which was previously allocated through hipMemCreate.

## Signature

```c
hipError_t hipMemRelease(hipMemGenericAllocationHandle_t handle);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `handle` | - handle of the memory allocation. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga4fe4c9887e5ce1ffd0f3d967f76ae91a)
