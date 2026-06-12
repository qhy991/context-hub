---
name: hip-hipipcgeteventhandle
description: "Gets an opaque interprocess handle for an event."
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

# hipIpcGetEventHandle

Gets an opaque interprocess handle for an event.

## Signature

```c
hipError_t hipIpcGetEventHandle(hipIpcEventHandle_t *handle, hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `handle` | Pointer to hipIpcEventHandle to return the opaque event handle |
| [in] | `event` | Event allocated with hipEventInterprocess and hipEventDisableTiming flags |

## Returns

hipSuccess , hipErrorInvalidConfiguration , hipErrorInvalidValue

## Notes

- This opaque handle may be copied into other processes and opened with hipIpcOpenEventHandle. Then hipEventRecord, hipEventSynchronize, hipStreamWaitEvent and hipEventQuery may be used in either process. Operations on the imported event after the exported event has been freed with hipEventDestroy will result in undefined behavior.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga16b63a461a72d22dbcbbdbdff548adba)
