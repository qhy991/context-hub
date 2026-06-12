---
name: hip-hiplibraryloaddata
description: "Load hip Library from inmemory object."
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

# hipLibraryLoadData

Load hip Library from inmemory object.

## Signature

```c
hipError_t hipLibraryLoadData(hipLibrary_t *library, const void *code, hipJitOption *jitOptions, void **jitOptionsValues, unsigned int numJitOptions, hipLibraryOption *libraryOptions, void **libraryOptionValues, unsigned int numLibraryOptions);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `library` | Output Library |
| [in] | `code` | In memory object |
| [in] | `jitOptions` | JIT options, CUDA only |
| [in] | `jitOptionsValues` | JIT options values, CUDA only |
| [in] | `numJitOptions` | Number of JIT options |
| [in] | `libraryOptions` | Library options |
| [in] | `libraryOptionValues` | Library options values |
| [in] | `numLibraryOptions` | Number of library options |

## Returns

hipSuccess , hipErrorInvalidValue ,

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gae417a022a086597d3e1f672c9015f4d5)
