---
name: hip-hipchoosedevice
description: "Device which matches hipDeviceProp_t is returned."
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

# hipChooseDevice

Device which matches hipDeviceProp_t is returned.

## Signature

```c
hipError_t hipChooseDevice(int *device, const hipDeviceProp_t *prop);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `device` | Pointer of the device |
| [in] | `prop` | Pointer of the properties |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gaf1e365e1d17cf40644d1470de4817c8e)
