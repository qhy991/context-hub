---
name: hip-hipdevicecanaccesspeer
description: "Determines if a device can access a peer device's memory."
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
  hw_unit: driver
  api_module: Peer to Peer Device Memory Access
---

# hipDeviceCanAccessPeer

Determines if a device can access a peer device's memory.

## Signature

```c
hipError_t hipDeviceCanAccessPeer(int *canAccessPeer, int deviceId, int peerDeviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `canAccessPeer` | - Returns the peer access capability (0 or 1) |
| [in] | `deviceId` | - The device accessing the peer device memory. |
| [in] | `peerDeviceId` | - Peer device where memory is physically located |

## Returns

hipSuccess , hipErrorInvalidDevice

## Notes

- The value of canAccessPeer ,
- Returns "1" if the specified deviceId is capable of directly accessing memory physically located on peerDeviceId ,
- Returns "0" if the specified deviceId is not capable of directly accessing memory physically located on peerDeviceId .
- Returns "0" if deviceId == peerDeviceId , both are valid devices, however, a device is not a peer of itself.
- Returns hipErrorInvalidDevice if deviceId or peerDeviceId are not valid devices

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___peer_to_peer.html#ga0a1c9ccd775758d9d7d5b5a1f525b719)
