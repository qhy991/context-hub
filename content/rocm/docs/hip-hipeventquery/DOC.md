---
name: hip-hipeventquery
description: "Query event status."
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

# hipEventQuery

Query event status.

## Signature

```c
hipError_t hipEventQuery(hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `event` | Event to query. |

## Returns

hipSuccess , hipErrorNotReady , hipErrorInvalidHandle , hipErrorInvalidValue , hipErrorNotInitialized , hipErrorLaunchFailure

## Notes

- Query the status of the specified event. This function will return hipSuccess if all commands in the appropriate stream (specified to hipEventRecord() ) have completed. If any execution has not completed, then hipErrorNotReady is returned.

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#ga5d12d7b798b5ceb5932d1ac21f5ac776)
