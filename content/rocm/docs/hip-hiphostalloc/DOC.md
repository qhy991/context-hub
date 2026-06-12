---
name: hip-hiphostalloc
description: "Allocate device accessible page locked host memory."
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

# hipHostAlloc

Allocate device accessible page locked host memory.

## Signature

```c
hipError_t hipHostAlloc(void **ptr, size_t size , unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | Pointer to the allocated host pinned memory |
| [in] | `size` | Requested memory size in bytes |
| [in] | `flags` | Type of host memory allocation see below |

## Returns

hipSuccess , hipErrorOutOfMemory , hipErrorInvalidValue

## Notes

- If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.
- Flags:

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga0e35f3397f6ea9c3f47a17461ae01231)
