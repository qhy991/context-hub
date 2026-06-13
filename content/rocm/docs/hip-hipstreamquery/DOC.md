---
name: hip-hipstreamquery
description: "Returns hipSuccess if all of the operations in the specified stream have completed, or hipErrorNotReady if not."
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

# hipStreamQuery

Returns hipSuccess if all of the operations in the specified stream have completed, or hipErrorNotReady if not.

## Signature

```c
hipError_t hipStreamQuery(hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to query |

## Returns

hipSuccess , hipErrorNotReady , hipErrorInvalidHandle

## Notes

- This is thread-safe and returns a snapshot of the current state of the queue. However, if other host threads are sending work to the stream, the status may change immediately after the function is called. It is typically used for debug.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga925b39ff78d3b5fd458bd9e2cade9f4e)
