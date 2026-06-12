---
name: hip-hipgetstreamdeviceid
description: "Returns device ID on the stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,callback-activity-apis
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Callback Activity APIs
---

# hipGetStreamDeviceId

Returns device ID on the stream.

## Signature

```c
hipError_t hipGetStreamDeviceId(hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream of device executed on. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___callback.html#gad16a23519ee4d7d87c7be53004b76608)
