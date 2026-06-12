---
name: hip-hipdevicegetpcibusid
description: "Returns a PCI Bus Id string for the device, overloaded to take int device ID."
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
  hw_unit: driver
  api_module: Initialization and Version
---

# hipDeviceGetPCIBusId

Returns a PCI Bus Id string for the device, overloaded to take int device ID.

## Signature

```c
hipError_t hipDeviceGetPCIBusId(char *pciBusId, int len, int device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pciBusId` | The string of PCI Bus Id format for the device |
| [in] | `len` | Maximum length of string |
| [in] | `device` | The device ordinal |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#gaaa961c8ec8047903617f4245fa50256a)
