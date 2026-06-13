---
name: hip-hipmemcpydtohasync
description: "Copy data from Device to Host asynchronously."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpyDtoHAsync

Copy data from Device to Host asynchronously.

## Signature

```c
hipError_t hipMemcpyDtoHAsync(void *dst, hipDeviceptr_t src, size_t sizeBytes, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being copy to |
| [in] | `src` | Data being copy from |
| [in] | `sizeBytes` | Data size in bytes |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad69da1994a646b843fb1fa465dbeb623)
