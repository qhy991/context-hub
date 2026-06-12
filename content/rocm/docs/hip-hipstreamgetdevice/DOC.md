---
name: hip-hipstreamgetdevice
description: "Gets the device associated with the stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Stream Management
---

# hipStreamGetDevice

Gets the device associated with the stream.

## Signature

```c
hipError_t hipStreamGetDevice(hipStream_t stream, hipDevice_t *device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to be queried |
| [out] | `device` | Device associated with the stream |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorContextIsDestroyed , hipErrorInvalidHandle , hipErrorNotInitialized , hipErrorDeinitialized , hipErrorInvalidContext

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga91b2d98f5530f0bd73a257fdca1abe4d)
