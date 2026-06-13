---
name: hip-hipdevicegetbypcibusid
description: "Returns a handle to a compute device."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,initialization-and-version
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Initialization and Version
---

# hipDeviceGetByPCIBusId

Returns a handle to a compute device.

## Signature

```c
hipError_t hipDeviceGetByPCIBusId(int *device, const char *pciBusId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `device` | The handle of the device |
| [in] | `pciBusId` | The string of PCI Bus Id for the device |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga2ec307f165d576c0c673a7b1fa9b0fe4)
