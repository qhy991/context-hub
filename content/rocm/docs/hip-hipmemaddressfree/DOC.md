---
name: hip-hipmemaddressfree
description: "Frees an address range reservation made via hipMemAddressReserve."
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
  hw_unit: driver
  api_module: Virtual Memory Management
---

# hipMemAddressFree

Frees an address range reservation made via hipMemAddressReserve.

## Signature

```c
hipError_t hipMemAddressFree(void * devPtr , size_t size);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `devPtr` | - starting address of the range. |
| [in] | `size` | - size of the range. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga0e8ce3b43894e908fb88c0a74d71cb32)
