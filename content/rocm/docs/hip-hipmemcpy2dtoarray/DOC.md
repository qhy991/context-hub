---
name: hip-hipmemcpy2dtoarray
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

# hipMemcpy2DToArray

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpy2DToArray(hipArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t spitch, size_t width , size_t height , hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Destination memory address |
| [in] | `wOffset` | Destination starting X offset |
| [in] | `hOffset` | Destination starting Y offset |
| [in] | `src` | Source memory address |
| [in] | `spitch` | Pitch of source memory |
| [in] | `width` | Width of matrix transfer (columns in bytes) |
| [in] | `height` | Height of matrix transfer (rows) |
| [in] | `kind` | Type of transfer |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaccf359cb35ce1887e6250c09e115e9a2)
