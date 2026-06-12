---
name: hip-hipmemcpyfromsymbolasync
description: "Copies data from the given symbol on the device asynchronously."
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

# hipMemcpyFromSymbolAsync

Copies data from the given symbol on the device asynchronously.

## Signature

```c
hipError_t hipMemcpyFromSymbolAsync(void *dst, const void *symbol, size_t sizeBytes, size_t offset, hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Returns pointer to destinition memory address |
| [in] | `symbol` | pointer to the symbole address on the device |
| [in] | `sizeBytes` | size in bytes to copy |
| [in] | `offset` | offset in bytes from the start of symbole |
| [in] | `kind` | type of memory transfer |
| [in] | `stream` | stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga50a9366e07b89172e140203a744a80c5)
