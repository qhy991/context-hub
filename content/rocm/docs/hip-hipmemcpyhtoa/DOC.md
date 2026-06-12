---
name: hip-hipmemcpyhtoa
description: "Copies data between host and device."
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

# hipMemcpyHtoA

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpyHtoA(hipArray_t dstArray, size_t dstOffset, const void *srcHost, size_t count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dstArray` | Destination memory address |
| [in] | `dstOffset` | Offset in bytes of destination array |
| [in] | `srcHost` | Source host pointer |
| [in] | `count` | Size of memory copy in bytes |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaaa6b5a61fa58239bb36344b219ed7e2c)
