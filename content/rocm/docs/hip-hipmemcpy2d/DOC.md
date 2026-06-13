---
name: hip-hipmemcpy2d
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

# hipMemcpy2D

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpy2D(void *dst, size_t dpitch, const void *src, size_t spitch, size_t width , size_t height , hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Destination memory address |
| [in] | `dpitch` | Pitch size in bytes of destination memory |
| [in] | `src` | Source memory address |
| [in] | `spitch` | Pitch size in bytes of source memory |
| [in] | `width` | Width size in bytes of matrix transfer (columns) |
| [in] | `height` | Height size in bytes of matrix transfer (rows) |
| [in] | `kind` | Type of transfer |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## Notes

- hipMemcpy2D supports memory matrix copy from the pointed area src to the pointed area dst. The copy direction is defined by kind which must be one of hipMemcpyHostToDevice , hipMemcpyHostToDevice , hipMemcpyDeviceToHost hipMemcpyDeviceToDevice or hipMemcpyDefault . Device to Device copies don't need to wait for host synchronization. The copy is executed on the default null tream. The src and dst must not overlap. dpitch and spitch are the widths in bytes in memory matrix, width cannot exceed dpitch or spitch.
- For hipMemcpy2D, the copy is always performed by the current device (set by hipSetDevice). For multi-gpu or peer-to-peer configurations, it is recommended to set the current device to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess with copy agent as the current device and src/dst as the peerDevice argument. if this is not done, the hipMemcpy2D will still work, but will perform the copy using a staging buffer on the host.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga8af4597ff0cd17247d8a857c4d8bfa8a)
