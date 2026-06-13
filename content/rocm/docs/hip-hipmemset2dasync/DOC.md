---
name: hip-hipmemset2dasync
description: "Fills asynchronously the memory area pointed to by dst with the constant value."
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

# hipMemset2DAsync

Fills asynchronously the memory area pointed to by dst with the constant value.

## Signature

```c
hipError_t hipMemset2DAsync(void *dst, size_t pitch , int value, size_t width , size_t height , hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Pointer to 2D device memory |
| [in] | `pitch` | Pitch size in bytes of 2D device memory, unused if height equals 1 |
| [in] | `value` | Value to set for each byte of specified memory |
| [in] | `width` | Width size in bytes in 2D memory |
| [in] | `height` | Height size in bytes in 2D memory |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga2bac47006b553a69424431c0445f8e95)
