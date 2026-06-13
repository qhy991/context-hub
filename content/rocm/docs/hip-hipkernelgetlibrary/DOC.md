---
name: hip-hipkernelgetlibrary
description: "Returns a Library Handle."
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

# hipKernelGetLibrary

Returns a Library Handle.

## Signature

```c
hipError_t hipKernelGetLibrary(hipLibrary_t *library, hipKernel_t kernel);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `library` | Returned Library handle |
| [in] | `kernel` | Kernel to retrieve library Handle |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gaeb1746abcfcbde455628f541c86f70fd)
