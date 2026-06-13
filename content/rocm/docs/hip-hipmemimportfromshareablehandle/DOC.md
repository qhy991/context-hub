---
name: hip-hipmemimportfromshareablehandle
description: "Imports an allocation from a requested shareable handle type."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,virtual-memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Virtual Memory Management
---

# hipMemImportFromShareableHandle

Imports an allocation from a requested shareable handle type.

## Signature

```c
hipError_t hipMemImportFromShareableHandle(hipMemGenericAllocationHandle_t *handle, void *osHandle, hipMemAllocationHandleType shHandleType);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `handle` | - returned value. |
| [in] | `osHandle` | - shareable handle representing the memory allocation. |
| [in] | `shHandleType` | - handle type. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#gacf32ac2b8aa367302c606a6eefadb4f1)
