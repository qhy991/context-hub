---
name: hip-hipstreamcreatewithpriority
description: "Creates an asynchronous stream with the specified priority."
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

# hipStreamCreateWithPriority

Creates an asynchronous stream with the specified priority.

## Signature

```c
hipError_t hipStreamCreateWithPriority(hipStream_t *stream, unsigned int flags, int priority);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `stream` | Pointer to new stream |
| [in] | `flags` | Parameters to control stream creation |
| [in] | `priority` | Priority of the stream. Lower numbers represent higher priorities. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Creates a new asynchronous stream with the specified priority, with its associated current device. stream returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, application must call hipStreamDestroy.
- The flags parameter controls behavior of the stream. The valid values are hipStreamDefault and hipStreamNonBlocking .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gace005d8ea734fb66c995bd43dac3fd44)
