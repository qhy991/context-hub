---
name: hip-hipmemcpy2dfromarrayasync
description: "Copies data between host and device asynchronously."
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

# hipMemcpy2DFromArrayAsync

Copies data between host and device asynchronously.

## Signature

```c
hipError_t hipMemcpy2DFromArrayAsync(void *dst, size_t dpitch, hipArray_const_t src, size_t wOffset, size_t hOffset, size_t width , size_t height , hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Destination memory address |
| [in] | `dpitch` | Pitch of destination memory |
| [in] | `src` | Source memory address |
| [in] | `wOffset` | Source starting X offset |
| [in] | `hOffset` | Source starting Y offset |
| [in] | `width` | Width of matrix transfer (columns in bytes) |
| [in] | `height` | Height of matrix transfer (rows) |
| [in] | `kind` | Type of transfer |
| [in] | `stream` | Accelerator view which the copy is being enqueued |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga946fe29e78ce1580cb95fa2210389263)
