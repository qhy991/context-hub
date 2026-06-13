---
name: hip-hipmemsetd16
description: "Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant short value value."
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

# hipMemsetD16

Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant short value value.

## Signature

```c
hipError_t hipMemsetD16(hipDeviceptr_t dest, unsigned short value, size_t count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dest` | Data ptr to be filled |
| [in] | `value` | Constant value to be set |
| [in] | `count` | Number of values to be set |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga3ee39cf8737f4a5d0e1e8c9eb870f02f)
