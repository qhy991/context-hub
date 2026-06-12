---
name: hip-hipgetdeviceflags
description: "Gets the flags set for current device."
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
  hw_unit: driver
  api_module: Device Management
---

# hipGetDeviceFlags

Gets the flags set for current device.

## Signature

```c
hipError_t hipGetDeviceFlags(unsigned int *flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `flags` | Pointer of the flags |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga1270f7281bb46cf3e077944e6f233d53)
