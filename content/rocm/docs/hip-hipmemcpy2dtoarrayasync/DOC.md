---
name: hip-hipmemcpy2dtoarrayasync
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

# hipMemcpy2DToArrayAsync

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpy2DToArrayAsync(hipArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t spitch, size_t width , size_t height , hipMemcpyKind kind, hipStream_t stream);
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
| [in] | `stream` | Accelerator view which the copy is being enqueued |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gab6953ee5f575d0324c19ffc51a72f8fb)
