---
name: hip-hipmemcpyatoa
description: "Copies from one 1D array to another."
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

# hipMemcpyAtoA

Copies from one 1D array to another.

## Signature

```c
hipError_t hipMemcpyAtoA(hipArray_t dstArray, size_t dstOffset, hipArray_t srcArray, size_t srcOffset, size_t ByteCount);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dstArray` | Destination array |
| [in] | `dstOffset` | Offset in bytes of destination array |
| [in] | `srcArray` | Source array |
| [in] | `srcOffset` | Offset in bytes of source array |
| [in] | `ByteCount` | Size of memory copy in bytes |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga0a714ba192b400688a1ccdd2b3359a9f)
