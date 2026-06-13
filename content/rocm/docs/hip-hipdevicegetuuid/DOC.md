---
name: hip-hipdevicegetuuid
description: "Returns an UUID for the device.[BETA]."
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

# hipDeviceGetUuid

Returns an UUID for the device.[BETA].

## Signature

```c
hipError_t hipDeviceGetUuid(hipUUID *uuid, hipDevice_t device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `uuid` | UUID for the device |
| [in] | `device` | device ordinal |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue , hipErrorNotInitialized , hipErrorDeinitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga70646553e01211704cf4d81312569d7d)
