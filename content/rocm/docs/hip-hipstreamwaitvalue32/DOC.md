---
name: hip-hipstreamwaitvalue32
description: "Enqueues a wait command to the stream.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-memory-operations
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Memory Operations
---

# hipStreamWaitValue32

Enqueues a wait command to the stream.[BETA].

## Signature

```c
hipError_t hipStreamWaitValue32(hipStream_t stream, void *ptr, uint32_t value, unsigned int flags, uint32_t mask);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream identifier |
| [in] | `ptr` | - Pointer to memory object allocated using hipMallocSignalMemory flag |
| [in] | `value` | - Value to be used in compare operation |
| [in] | `flags` | - Defines the compare operation, supported values are hipStreamWaitValueGte hipStreamWaitValueEq , hipStreamWaitValueAnd and hipStreamWaitValueNor |
| [in] | `mask` | - Mask to be applied on value at memory before it is compared with value, default value is set to enable every bit |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Enqueues a wait command to the stream, all operations enqueued on this stream after this, will not execute until the defined wait condition is true.
- hipStreamWaitValueGte : waits until *ptr&amp;mask &gt;= value
- hipStreamWaitValueEq : waits until *ptr&amp;mask == value
- hipStreamWaitValueAnd : waits until ((*ptr&amp;mask) &amp; value) != 0
- hipStreamWaitValueNor : waits until ~((*ptr&amp;mask) | (value&amp;mask)) != 0

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#gafade0b118c7ed28e1dae21cd4df0a9d6)
