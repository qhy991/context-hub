---
name: hip-hipsetdevice
description: "Set default device to be used for subsequent hip API calls from this thread."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,device-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Device Management
---

# hipSetDevice

Set default device to be used for subsequent hip API calls from this thread.

## Signature

```c
hipError_t hipSetDevice(int deviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `deviceId` | Valid device in range 0... hipGetDeviceCount() . |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorNoDevice

## Notes

- Sets device as the default device for the calling host thread. Valid device id's are 0... ( hipGetDeviceCount() -1).
- Many HIP APIs implicitly use the "default device" :
- This function may be called from any host thread. Multiple host threads may use the same device. This function does no synchronization with the previous or new device, and has very little runtime overhead. Applications can use hipSetDevice to quickly switch the default device before making a HIP runtime call which uses the default device.
- The default device is stored in thread-local-storage for each thread. Thread-pool implementations may inherit the default device of the previous thread. A good practice is to always call hipSetDevice at the start of HIP coding sequency to establish a known standard device.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga43c1e7f15925eeb762195ccb5e063eae)
