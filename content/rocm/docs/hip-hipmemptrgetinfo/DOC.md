---
name: hip-hipmemptrgetinfo
description: "Get allocated memory size via memory pointer."
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

# hipMemPtrGetInfo

Get allocated memory size via memory pointer.

## Signature

```c
hipError_t hipMemPtrGetInfo(void *ptr, size_t * size);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `ptr` | Pointer to allocated memory |
| [out] | `size` | Returns the allocated memory size in bytes |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- This function gets the allocated shared virtual memory size from memory pointer.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaf7e9522b8fd7bae6cc1bf2e3238fd20f)
