---
name: hip-hipmemset3d
description: "Fills synchronously the memory area pointed to by pitchedDevPtr with the constant value."
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

# hipMemset3D

Fills synchronously the memory area pointed to by pitchedDevPtr with the constant value.

## Signature

```c
hipError_t hipMemset3D(hipPitchedPtr pitchedDevPtr, int value, hipExtent extent);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `pitchedDevPtr` | Pointer to pitched device memory |
| [in] | `value` | Value to set for each byte of specified memory |
| [in] | `extent` | Size parameters for width field in bytes in device memory |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga3c04a21c9de9c55b3e47d8c87a0b0593)
