---
name: hip-hipmemcpy2dasync
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
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpy2DAsync

Copies data between host and device asynchronously.

## Signature

```c
hipError_t hipMemcpy2DAsync(void *dst, size_t dpitch, const void *src, size_t spitch, size_t width , size_t height , hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Pointer to destination memory address |
| [in] | `dpitch` | Pitch size in bytes of destination memory |
| [in] | `src` | Pointer to source memory address |
| [in] | `spitch` | Pitch size in bytes of source memory |
| [in] | `width` | Width of matrix transfer (columns in bytes) |
| [in] | `height` | Height of matrix transfer (rows) |
| [in] | `kind` | Type of transfer |
| [in] | `stream` | Stream to use |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## Notes

- hipMemcpy2DAsync supports memory matrix copy from the pointed area src to the pointed area dst. The copy direction is defined by kind which must be one of hipMemcpyHostToDevice , hipMemcpyDeviceToHost , hipMemcpyDeviceToDevice or hipMemcpyDefault . dpitch and spitch are the widths in bytes for memory matrix corresponds to dst and src. width cannot exceed dpitch or spitch.
- The copy is always performed by the device associated with the specified stream. The API is asynchronous with respect to the host, so the call may return before the copy is complete. The copy can optionally be excuted in a specific stream by passing a non-zero stream argument, for HostToDevice or DeviceToHost copies, the copy can overlap with operations in other streams.
- For multi-gpu or peer-to-peer configurations, it is recommended to use a stream which is attached to the device where the src data is physically located.
- For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess) with copy agent as the current device and src/dst as the peerDevice argument. If enabling device peer access is not done, the API will still work, but will perform the copy using a staging buffer on the host.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga6b9eaa58bc332346cb8ed956f8b590ac)
