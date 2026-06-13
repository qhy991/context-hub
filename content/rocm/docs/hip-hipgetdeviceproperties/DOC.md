---
name: hip-hipgetdeviceproperties
description: "Returns device properties."
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

# hipGetDeviceProperties

Returns device properties.

## Signature

```c
hipError_t hipGetDeviceProperties(hipDeviceProp_t *prop, int deviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `prop` | written with device properties |
| [in] | `deviceId` | which device to query for information |

## Returns

hipSuccess , hipErrorInvalidDevice

## Notes

- Populates hipGetDeviceProperties with information for the specified device.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga32208513b7cd491f0cb5fc884053f790)
