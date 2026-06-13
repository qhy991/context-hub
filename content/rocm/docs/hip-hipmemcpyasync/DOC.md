---
name: hip-hipmemcpyasync
description: "Copies data from src to dst asynchronously."
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

# hipMemcpyAsync

Copies data from src to dst asynchronously.

## Signature

```c
hipError_t hipMemcpyAsync(void *dst, const void *src, size_t sizeBytes, hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being copy to |
| [in] | `src` | Data being copy from |
| [in] | `sizeBytes` | Data size in bytes |
| [in] | `kind` | Type of memory transfer |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorUnknown

## Notes

- The copy is always performed by the device associated with the specified stream.
- For multi-gpu or peer-to-peer configurations, it is recommended to use a stream which is attached to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess) with copy agent as the current device and src/dest as the peerDevice argument. If enabling device peer access is not done, the memory copy will still work, but will perform the copy using a staging buffer on the host.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad55fa9f5980b711bc93c52820149ba18)
