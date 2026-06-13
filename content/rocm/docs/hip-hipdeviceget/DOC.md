---
name: hip-hipdeviceget
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

# hipDeviceGet

Returns a handle to a compute device.

## Signature

```c
hipError_t hipDeviceGet(hipDevice_t *device, int ordinal);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `device` | Handle of device |
| [in] | `ordinal` | Device ordinal |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#gadf6c74aaf7c22fea80e9ac3400d43704)
