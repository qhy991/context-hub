---
name: hip-hipmemset
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemset

Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value.

## Signature

```c
hipError_t hipMemset(void *dst, int value, size_t sizeBytes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being filled |
| [in] | `value` | Value to be set |
| [in] | `sizeBytes` | Data size in bytes |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gac7441e74affcce4b8b69dba996c5ebc4)
