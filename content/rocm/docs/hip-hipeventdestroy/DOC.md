---
name: hip-hipeventdestroy
description: "Destroy the specified event."
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

# hipEventDestroy

Destroy the specified event.

## Signature

```c
hipError_t hipEventDestroy(hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `event` | Event to destroy. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue , hipErrorLaunchFailure

## Notes

- Releases memory associated with the event. If the event is recording but has not completed recording when hipEventDestroy() is called, the function will return immediately and the completion_future resources will be released later, when the hipDevice is synchronized.

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#ga83260357dce0c39e8c6a3c74ec97484c)
