---
name: hip-hipmemexporttoshareablehandle
description: "Exports an allocation to a requested shareable handle type."
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

# hipMemExportToShareableHandle

Exports an allocation to a requested shareable handle type.

## Signature

```c
hipError_t hipMemExportToShareableHandle(void *shareableHandle, hipMemGenericAllocationHandle_t handle, hipMemAllocationHandleType handleType, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `shareableHandle` | - value of the returned handle. |
| [in] | `handle` | - handle to share. |
| [in] | `handleType` | - type of the shareable handle. |
| [in] | `flags` | - currently unused, must be zero. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga248353e17dd95b4514d8ee979cc07175)
