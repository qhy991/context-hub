---
name: hip-hipeventsynchronize
description: "Wait for an event to complete."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Event Management
---

# hipEventSynchronize

Wait for an event to complete.

## Signature

```c
hipError_t hipEventSynchronize(hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `event` | Event on which to wait. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized , hipErrorInvalidHandle , hipErrorLaunchFailure

## Notes

- This function will block until the event is ready, waiting for all previous work in the stream specified when event was recorded with hipEventRecord() .
- If hipEventRecord() has not been called on event , this function returns hipSuccess when no event is captured.

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#ga1f72d98ba5d6f7dc3da54e0c41fe38b1)
