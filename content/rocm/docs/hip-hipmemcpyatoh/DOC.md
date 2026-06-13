---
name: hip-hipmemcpyatoh
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpyAtoH

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpyAtoH(void *dst, hipArray_t srcArray, size_t srcOffset, size_t count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Destination memory address |
| [in] | `srcArray` | Source array |
| [in] | `srcOffset` | Offset in bytes of source array |
| [in] | `count` | Size of memory copy in bytes |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gabf833a230a7883199514e3fe7face896)
