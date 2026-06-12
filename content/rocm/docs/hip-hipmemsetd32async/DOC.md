---
name: hip-hipmemsetd32async
description: "Fills the memory area pointed to by dev with the constant integer value for specified number of times."
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

# hipMemsetD32Async

Fills the memory area pointed to by dev with the constant integer value for specified number of times.

## Signature

```c
hipError_t hipMemsetD32Async(hipDeviceptr_t dst, int value, size_t count, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Pointer to device memory |
| [in] | `value` | Value to set for each byte of specified memory |
| [in] | `count` | Number of values to be set |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- hipMemsetD32Async() is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gae0e29827e32436fc6f0431b865e32244)
