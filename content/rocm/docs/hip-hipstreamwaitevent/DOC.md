---
name: hip-hipstreamwaitevent
description: "Makes the specified compute stream wait for the specified event."
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

# hipStreamWaitEvent

Makes the specified compute stream wait for the specified event.

## Signature

```c
hipError_t hipStreamWaitEvent(hipStream_t stream, hipEvent_t event, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to make wait |
| [in] | `event` | Event to wait on |
| [in] | `flags` | Parameters to control the operation |

## Returns

hipSuccess , hipErrorInvalidHandle , hipErrorInvalidValue , hipErrorStreamCaptureIsolation

## Notes

- This function inserts a wait operation into the specified stream. All future work submitted to stream will wait until event reports completion before beginning execution.
- Flags include: hipEventWaitDefault: Default event creation flag. hipEventWaitExternal: Wait is captured in the graph as an external event node when performing stream capture
- This function only waits for commands in the current stream to complete. Notably, this function does not implicitly wait for commands in the default stream to complete, even if the specified stream is created with hipStreamNonBlocking = 0.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gacdd84c8f8ef1539c96c57c1d5bcae633)
