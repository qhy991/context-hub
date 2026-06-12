---
name: hip-hipmemcpy2darraytoarray
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

# hipMemcpy2DArrayToArray

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpy2DArrayToArray(hipArray_t dst, size_t wOffsetDst, size_t hOffsetDst, hipArray_const_t src, size_t wOffsetSrc, size_t hOffsetSrc, size_t width , size_t height , hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Destination memory address |
| [in] | `wOffsetDst` | Destination starting X offset |
| [in] | `hOffsetDst` | Destination starting Y offset |
| [in] | `src` | Source memory address |
| [in] | `wOffsetSrc` | Source starting X offset |
| [in] | `hOffsetSrc` | Source starting Y offset (columns in bytes) |
| [in] | `width` | Width of matrix transfer (columns in bytes) |
| [in] | `height` | Height of matrix transfer (rows) |
| [in] | `kind` | Type of transfer |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga11a0bead0f40a85a212f8a686b72b243)
