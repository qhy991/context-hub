---
name: hip-hipmemaddressreserve
description: "Reserves an address range."
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

# hipMemAddressReserve

Reserves an address range.

## Signature

```c
hipError_t hipMemAddressReserve(void **ptr, size_t size , size_t alignment, void *addr, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | - starting address of the reserved range. |
| [in] | `size` | - size of the reservation. |
| [in] | `alignment` | - alignment of the address. |
| [in] | `addr` | - requested starting address of the range. |
| [in] | `flags` | - currently unused, must be zero. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#gaa9787c99a5a2db730bfc392a2ff3de18)
