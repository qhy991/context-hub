---
name: hip-hiplaunchhostfunc
description: "Enqueues a host function call in a stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,launch-api
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Launch API
---

# hipLaunchHostFunc

Enqueues a host function call in a stream.

## Signature

```c
hipError_t hipLaunchHostFunc(hipStream_t stream, hipHostFn_t fn, void *userData);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - The stream to enqueue work in. |
| [in] | `fn` | - The function to call once enqueued preceeding operations are complete. |
| [in] | `userData` | - User-specified data to be passed to the function. |

## Returns

hipSuccess , hipErrorInvalidResourceHandle , hipErrorInvalidValue , hipErrorNotSupported

## Notes

- The host function to call in this API will be executed after the preceding operations in the stream are complete. The function is a blocking operation that blocks operations in the stream that follow it, until the function is returned. Event synchronization and internal callback functions make sure enqueued operations will execute in order, in the stream.
- The host function must not make any HIP API calls. The host function is non-reentrant. It must not perform sychronization with any operation that may depend on other processing execution but is not enqueued to run earlier in the stream.
- Host functions that are enqueued respectively in different non-blocking streams can run concurrently.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#ga154cd475c8e1b9e623981fc165c543a9)
