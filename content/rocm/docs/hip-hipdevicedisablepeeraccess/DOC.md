---
name: hip-hipdevicedisablepeeraccess
description: "Disables direct access to memory allocations on a peer device."
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

# hipDeviceDisablePeerAccess

Disables direct access to memory allocations on a peer device.

## Signature

```c
hipError_t hipDeviceDisablePeerAccess(int peerDeviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `peerDeviceId` | Peer device to disable direct access to |

## Returns

hipSuccess , hipErrorPeerAccessNotEnabled

## Notes

- If direct access to memory allocations on peer device has not been enabled yet from the current device, it returns hipErrorPeerAccessNotEnabled .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___peer_to_peer.html#ga85030c72824fb60aaddc7374ab60481b)
