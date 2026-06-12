---
name: hip-hipstreamdestroy
description: "Destroys the specified stream."
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
  hw_unit: driver
  api_module: Stream Management
---

# hipStreamDestroy

Destroys the specified stream.

## Signature

```c
hipError_t hipStreamDestroy(hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess hipErrorInvalidHandle

## Notes

- Destroys the specified stream.
- If commands are still executing on the specified stream, some may complete execution before the queue is deleted.
- The queue may be destroyed while some commands are still inflight, or may wait for all commands queued to the stream before destroying it.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga3076a3499ed2c7821311006100bb95ec)
