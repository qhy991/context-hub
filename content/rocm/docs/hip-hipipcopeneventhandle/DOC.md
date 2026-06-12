---
name: hip-hipipcopeneventhandle
description: "Opens an interprocess event handles."
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

# hipIpcOpenEventHandle

Opens an interprocess event handles.

## Signature

```c
hipError_t hipIpcOpenEventHandle(hipEvent_t *event, hipIpcEventHandle_t handle);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `event` | Pointer to hipEvent_t to return the event |
| [in] | `handle` | The opaque interprocess handle to open |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidContext

## Notes

- Opens an interprocess event handle exported from another process with hipIpcGetEventHandle. The returned hipEvent_t behaves like a locally created event with the hipEventDisableTiming flag specified. This event need be freed with hipEventDestroy. Operations on the imported event after the exported event has been freed with hipEventDestroy will result in undefined behavior. If the function is called within the same process where handle is returned by hipIpcGetEventHandle, it will return hipErrorInvalidContext.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gae73ef28488c43e5343fdf02178c25a5d)
