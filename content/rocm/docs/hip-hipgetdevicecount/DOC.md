---
name: hip-hipgetdevicecount
description: "Return number of compute-capable devices."
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

# hipGetDeviceCount

Return number of compute-capable devices.

## Signature

```c
hipError_t hipGetDeviceCount(int *count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `count` | Returns number of compute-capable devices. |

## Returns

hipSuccess , hipErrorNoDevice

## Notes

- Returns in *count the number of devices that have ability to run compute commands. If there are no such devices, then hipGetDeviceCount will return hipErrorNoDevice . If 1 or more devices can be found, then hipGetDeviceCount returns hipSuccess .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga8555d5c76d88c50ddbf54ae70b568394)
