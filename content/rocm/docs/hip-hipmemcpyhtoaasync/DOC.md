---
name: hip-hipmemcpyhtoaasync
description: "Copies from host memory to a 1D array."
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

# hipMemcpyHtoAAsync

Copies from host memory to a 1D array.

## Signature

```c
hipError_t hipMemcpyHtoAAsync(hipArray_t dstArray, size_t dstOffset, const void *srcHost, size_t ByteCount, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dstArray` | Destination array |
| [in] | `dstOffset` | Offset in bytes of destination array |
| [in] | `srcHost` | Source host pointer |
| [in] | `ByteCount` | Size of memory copy in bytes |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga7458d07076c60e26707ea0522da8e694)
