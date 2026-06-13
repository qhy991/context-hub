---
name: hip-hipmemset3dasync
description: "Fills asynchronously the memory area pointed to by pitchedDevPtr with the constant value."
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

# hipMemset3DAsync

Fills asynchronously the memory area pointed to by pitchedDevPtr with the constant value.

## Signature

```c
hipError_t hipMemset3DAsync(hipPitchedPtr pitchedDevPtr, int value, hipExtent extent, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `pitchedDevPtr` | Pointer to pitched device memory |
| [in] | `value` | Value to set for each byte of specified memory |
| [in] | `extent` | Size parameters for width field in bytes in device memory |
| [in] | `stream` | Stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga5565cddc90c7ebd0f8b081d5440b3166)
