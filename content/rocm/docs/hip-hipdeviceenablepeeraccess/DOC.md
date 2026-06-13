---
name: hip-hipdeviceenablepeeraccess
description: "Enables direct access to memory allocations on a peer device."
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

# hipDeviceEnablePeerAccess

Enables direct access to memory allocations on a peer device.

## Signature

```c
hipError_t hipDeviceEnablePeerAccess(int peerDeviceId, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `peerDeviceId` | - Peer device to enable direct access to from the current device |
| [in] | `flags` | - Reserved for future use, must be zero |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue ,

## Notes

- When this API is successful, all memory allocations on peer device will be mapped into the address space of the current device. In addition, any future memory allocation on the peer device will remain accessible from the current device, until the access is disabled using hipDeviceDisablePeerAccess or device is reset using hipDeviceReset.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___peer_to_peer.html#ga0caca59034134d7a7bb893cc1caa653e)
