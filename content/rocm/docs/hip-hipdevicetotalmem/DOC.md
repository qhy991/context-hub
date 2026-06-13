---
name: hip-hipdevicetotalmem
description: "Returns the total amount of memory on the device."
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

# hipDeviceTotalMem

Returns the total amount of memory on the device.

## Signature

```c
hipError_t hipDeviceTotalMem(size_t *bytes, hipDevice_t device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `bytes` | The size of memory in bytes, on the device |
| [in] | `device` | The ordinal of the device |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga8991e535d0ef1ead0524e73364623041)
