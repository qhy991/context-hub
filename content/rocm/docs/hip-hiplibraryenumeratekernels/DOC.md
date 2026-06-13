---
name: hip-hiplibraryenumeratekernels
description: "Retrieve kernel handles within a library."
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

# hipLibraryEnumerateKernels

Retrieve kernel handles within a library.

## Signature

```c
hipError_t hipLibraryEnumerateKernels(hipKernel_t *kernels, unsigned int numKernels, hipLibrary_t library);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `kernels` | Buffer for kernel handles |
| [in] | `numKernels` | Maximum number of kernel handles to return to buffer @oaram [in] library Library handle to query from |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga698bf2365bcb3ab7380bc81dd8033667)
