---
name: hip-hiplibraryunload
description: "Unload HIP Library."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,module-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Module Management
---

# hipLibraryUnload

Unload HIP Library.

## Signature

```c
hipError_t hipLibraryUnload(hipLibrary_t library);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `library` | Input created hip library |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga3fd2267120accdaf3aa0c6cc684d7e1d)
