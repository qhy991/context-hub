---
name: hip-hipgetdevice
description: "Return the default device id for the calling host thread."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Device Management
---

# hipGetDevice

Return the default device id for the calling host thread.

## Signature

```c
hipError_t hipGetDevice(int *deviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `deviceId` | *device is written with the default device |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## Notes

- HIP maintains an default device for each thread using thread-local-storage. This device is used implicitly for HIP runtime APIs called by this thread. hipGetDevice returns in * device the default device for the calling host thread.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga7e0e2e8c5f78e3c7449764657c254e0a)
