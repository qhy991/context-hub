---
name: hip-hipgetsymboladdress
description: "Gets device pointer associated with symbol on the device."
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

# hipGetSymbolAddress

Gets device pointer associated with symbol on the device.

## Signature

```c
hipError_t hipGetSymbolAddress(void ** devPtr , const void *symbol);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `devPtr` | pointer to the device associated the symbole |
| [in] | `symbol` | pointer to the symbole of the device |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaecac468bcedcfb139058df2d83d38987)
