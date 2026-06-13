---
name: hip-hipmemcpyfromsymbol
description: "Copies data from the given symbol on the device."
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

# hipMemcpyFromSymbol

Copies data from the given symbol on the device.

## Signature

```c
hipError_t hipMemcpyFromSymbol(void *dst, const void *symbol, size_t sizeBytes, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Returns pointer to destinition memory address |
| [in] | `symbol` | Pointer to the symbole address on the device |
| [in] | `sizeBytes` | Size in bytes to copy |
| [in] | `offset` | Offset in bytes from the start of symbole |
| [in] | `kind` | Type of memory transfer |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga5e06c171bb33ac109bf9e642bea57314)
