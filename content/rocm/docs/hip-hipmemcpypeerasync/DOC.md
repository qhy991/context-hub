---
name: hip-hipmemcpypeerasync
description: "Copies memory between two peer accessible devices asynchronously."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,peer-to-peer-device-memory-access
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Peer to Peer Device Memory Access
---

# hipMemcpyPeerAsync

Copies memory between two peer accessible devices asynchronously.

## Signature

```c
hipError_t hipMemcpyPeerAsync(void *dst, int dstDeviceId, const void *src, int srcDevice, size_t sizeBytes, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | - Destination device pointer |
| [in] | `dstDeviceId` | - Destination device |
| [in] | `src` | - Source device pointer |
| [in] | `srcDevice` | - Source device |
| [in] | `sizeBytes` | - Size of memory copy in bytes |
| [in] | `stream` | - Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___peer_to_peer.html#ga60091a115da3cb616adef5741fab4c4e)
