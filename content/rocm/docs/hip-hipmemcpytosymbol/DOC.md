---
name: hip-hipmemcpytosymbol
description: "Copies data to the given symbol on the device. Symbol HIP APIs allow a kernel to define a device-side data symbol which can be accessed on the host side. The symbol can be in __constant or device space. Note that the symbol name needs to be encased in the HIP_SYMBOL macro. This also applies to hipMemcpyFromSymbol, hipGetSymbolAddress, and hipGetSymbolSize. For detailed usage, see the memcpyToSymbol example in the HIP Porting Guide."
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

# hipMemcpyToSymbol

Copies data to the given symbol on the device. Symbol HIP APIs allow a kernel to define a device-side data symbol which can be accessed on the host side. The symbol can be in __constant or device space. Note that the symbol name needs to be encased in the HIP_SYMBOL macro. This also applies to hipMemcpyFromSymbol, hipGetSymbolAddress, and hipGetSymbolSize. For detailed usage, see the memcpyToSymbol example in the HIP Porting Guide.

## Signature

```c
hipError_t hipMemcpyToSymbol(const void *symbol, const void *src, size_t sizeBytes, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `symbol` | pointer to the device symbole |
| [in] | `src` | pointer to the source address |
| [in] | `sizeBytes` | size in bytes to copy |
| [in] | `offset` | offset in bytes from start of symbole |
| [in] | `kind` | type of memory transfer |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gac0d988981c8535af1712f1f57436869b)
