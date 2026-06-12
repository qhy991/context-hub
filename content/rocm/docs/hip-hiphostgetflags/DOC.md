---
name: hip-hiphostgetflags
description: "Return flags associated with host pointer."
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

# hipHostGetFlags

Return flags associated with host pointer.

## Signature

```c
hipError_t hipHostGetFlags(unsigned int *flagsPtr, void *hostPtr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `flagsPtr` | Memory location to store flags |
| [in] | `hostPtr` | Host Pointer allocated through hipHostMalloc |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga4d26915873b3e3534ceb4dc310f8709a)
