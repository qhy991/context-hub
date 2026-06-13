---
name: hip-hiplibrarygetkernel
description: "Get Kernel object from library."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Module Management
---

# hipLibraryGetKernel

Get Kernel object from library.

## Signature

```c
hipError_t hipLibraryGetKernel(hipKernel_t *pKernel, hipLibrary_t library, const char *name);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pKernel` | Output kernel object |
| [in] | `library` | Input hip library |
| [in] | `name` | kernel name to be searched for |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga8802b7f1757161e47238dc32cceb9283)
