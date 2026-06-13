---
name: hip-hipdevicegetstreampriorityrange
description: "Returns numerical values that correspond to the least and greatest stream priority."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Management
---

# hipDeviceGetStreamPriorityRange

Returns numerical values that correspond to the least and greatest stream priority.

## Signature

```c
hipError_t hipDeviceGetStreamPriorityRange(int *leastPriority, int *greatestPriority);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `leastPriority` | Pointer in which a value corresponding to least priority is returned. |
| [in,out] | `greatestPriority` | Pointer in which a value corresponding to greatest priority is returned. |

## Returns

hipSuccess

## Notes

- Returns in *leastPriority and *greatestPriority the numerical values that correspond to the least and greatest stream priority respectively. Stream priorities follow a convention where lower numbers imply greater priorities. The range of meaningful stream priorities is given by [*leastPriority,*greatestPriority]. If the user attempts to create a stream with a priority value that is outside the meaningful range as specified by this API, the priority is automatically clamped to within the valid range.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga2b0709fb23b273abec8ea223ebb362bc)
