---
name: hip-hipmemgetaccess
description: "Get the access flags set for the given location and ptr."
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

# hipMemGetAccess

Get the access flags set for the given location and ptr.

## Signature

```c
hipError_t hipMemGetAccess(unsigned long long *flags, const hipMemLocation *location, void *ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `flags` | - flags for this location. |
| [in] | `location` | - target location. |
| [in] | `ptr` | - address to check the access flags. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#ga41b61f25f37df6b86084e09f7906c74b)
