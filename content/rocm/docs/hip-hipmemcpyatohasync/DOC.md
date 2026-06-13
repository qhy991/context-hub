---
name: hip-hipmemcpyatohasync
description: "Copies from one 1D array to host memory."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpyAtoHAsync

Copies from one 1D array to host memory.

## Signature

```c
hipError_t hipMemcpyAtoHAsync(void *dstHost, hipArray_t srcArray, size_t srcOffset, size_t ByteCount, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dstHost` | Destination pointer |
| [in] | `srcArray` | Source array |
| [in] | `srcOffset` | Offset in bytes of source array |
| [in] | `ByteCount` | Size of memory copy in bytes |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga25614799894ee316c4ce832a57a29741)
