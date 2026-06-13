---
name: hip-hipdevicecomputecapability
description: "Returns the compute capability of the device."
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

# hipDeviceComputeCapability

Returns the compute capability of the device.

## Signature

```c
hipError_t hipDeviceComputeCapability(int *major, int *minor, hipDevice_t device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `major` | Major compute capability version number |
| [out] | `minor` | Minor compute capability version number |
| [in] | `device` | Device ordinal |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga0a1cf94d2b571ca3279577d5af0d1672)
