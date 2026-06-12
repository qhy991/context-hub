---
name: hip-hipeventrecord
description: "Record an event in the specified stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,event-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Event Management
---

# hipEventRecord

Record an event in the specified stream.

## Signature

```c
hipError_t hipEventRecord(hipEvent_t event, hipStream_t stream=NULL);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `event` | event to record. |
| [in] | `stream` | stream in which to record event. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized , hipErrorInvalidHandle , hipErrorLaunchFailure

## Notes

- hipEventQuery() or hipEventSynchronize() must be used to determine when the event transitions from "recording" (after hipEventRecord() is called) to "recorded" (when timestamps are set, if requested).
- Events which are recorded in a non-NULL stream will transition to from recording to "recorded" state when they reach the head of the specified stream, after all previous commands in that stream have completed executing.
- If hipEventRecord() has been previously called on this event, then this call will overwrite any existing state in event.
- If this function is called on an event that is currently being recorded, results are undefined

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#gace88ebd8c7ec42a6c2cebda2e8b0cb38)
