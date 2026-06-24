---
name: hip-hipeventelapsedtime
description: "Return the elapsed time between two events."
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

# hipEventElapsedTime

Return the elapsed time between two events.

## Signature

```c
hipError_t hipEventElapsedTime(float *ms, hipEvent_t start, hipEvent_t stop);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ms` | : Return time between start and stop in ms. |
| [in] | `start` | : Start event. |
| [in] | `stop` | : Stop event. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotReady , hipErrorInvalidHandle , hipErrorNotInitialized , hipErrorLaunchFailure

## Notes

- Computes the elapsed time between two events. Time is computed in ms, with a resolution of approximately 1 us.
- Events which are recorded in a NULL stream will block until all commands on all other streams complete execution, and then record the timestamp.
- Events which are recorded in a non-NULL stream will record their timestamp when they reach the head of the specified stream, after all previous commands in that stream have completed executing. Thus the time that the event recorded may be significantly after the host calls hipEventRecord() .
- If hipEventRecord() has not been called on either event, then hipErrorInvalidHandle is returned. If hipEventRecord() has been called on both events, but the timestamp has not yet been recorded on one or both events (that is, hipEventQuery() would return hipErrorNotReady on at least one of the events), then hipErrorNotReady is returned.

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#gad4128b815cb475c8e13c7e66ff6250b7)

## Semantics
Calculates the execution time (in milliseconds) elapsed between two recorded events. Resolves the difference between the GPU hardware timestamps captured when the start and stop events were signaled.

## Example
```cpp
#include <hip/hip_runtime.h>
#include <iostream>

void measure_time(hipEvent_t start, hipEvent_t stop) {
    float ms = 0.0f;
    hipEventElapsedTime(&ms, start, stop);
    std::cout << "Kernel took " << ms << " ms" << std::endl;
}
```
