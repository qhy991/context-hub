---
name: hip-hipmemsetd8async
description: "Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Memory Management
---

# hipMemsetD8Async

Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value.

## Signature

```c
hipError_t hipMemsetD8Async(hipDeviceptr_t dest, unsigned char value, size_t count, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dest` | Data ptr to be filled |
| [in] | `value` | Constant value to be set |
| [in] | `count` | Number of values to be set |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized

## Notes

- hipMemsetD8Async() is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga11b214a1af7b60f85694331802dd557c)
