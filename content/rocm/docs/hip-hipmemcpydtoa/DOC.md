---
name: hip-hipmemcpydtoa
description: "Copies from device memory to a 1D array."
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

# hipMemcpyDtoA

Copies from device memory to a 1D array.

## Signature

```c
hipError_t hipMemcpyDtoA(hipArray_t dstArray, size_t dstOffset, hipDeviceptr_t srcDevice, size_t ByteCount);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dstArray` | Destination array |
| [in] | `dstOffset` | Offset in bytes of destination array |
| [in] | `srcDevice` | Source device pointer |
| [in] | `ByteCount` | Size of memory copy in bytes |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga91e920637e005ddec51610ef38b55285)
