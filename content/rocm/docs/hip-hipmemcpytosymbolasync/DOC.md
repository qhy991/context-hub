---
name: hip-hipmemcpytosymbolasync
description: "Copies data to the given symbol on the device asynchronously."
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

# hipMemcpyToSymbolAsync

Copies data to the given symbol on the device asynchronously.

## Signature

```c
hipError_t hipMemcpyToSymbolAsync(const void *symbol, const void *src, size_t sizeBytes, size_t offset, hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `symbol` | pointer to the device symbole |
| [in] | `src` | pointer to the source address |
| [in] | `sizeBytes` | size in bytes to copy |
| [in] | `offset` | offset in bytes from start of symbole |
| [in] | `kind` | type of memory transfer |
| [in] | `stream` | stream identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaaceb6e89fb822d3a8e387b526b718478)
