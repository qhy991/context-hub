---
name: hip-hipmemmap
description: "Maps an allocation handle to a reserved virtual address range."
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

# hipMemMap

Maps an allocation handle to a reserved virtual address range.

## Signature

```c
hipError_t hipMemMap(void *ptr, size_t size , size_t offset, hipMemGenericAllocationHandle_t handle, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `ptr` | - address where the memory will be mapped. |
| [in] | `size` | - size of the mapping. |
| [in] | `offset` | - offset into the memory, currently must be zero. |
| [in] | `handle` | - memory allocation to be mapped. |
| [in] | `flags` | - currently unused, must be zero. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#gaa921e5167a69151f8e89d3e61ae811b7)
