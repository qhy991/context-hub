---
name: hip-hipgetsymbolsize
description: "Gets the size of the given symbol on the device."
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

# hipGetSymbolSize

Gets the size of the given symbol on the device.

## Signature

```c
hipError_t hipGetSymbolSize(size_t * size , const void *symbol);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `symbol` | pointer to the device symbole |
| [out] | `size` | pointer to the size |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gae61bb9a71f0fe9b3eee29336d6b83d97)
