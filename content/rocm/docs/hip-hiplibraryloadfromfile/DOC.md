---
name: hip-hiplibraryloadfromfile
description: "Load hip Library from file."
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

# hipLibraryLoadFromFile

Load hip Library from file.

## Signature

```c
hipError_t hipLibraryLoadFromFile(hipLibrary_t *library, const char *fileName, hipJitOption *jitOptions, void **jitOptionsValues, unsigned int numJitOptions, hipLibraryOption *libraryOptions, void **libraryOptionValues, unsigned int numLibraryOptions);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `library` | Output Library |
| [in] | `fileName` | file which contains code object |
| [in] | `jitOptions` | JIT options, CUDA only |
| [in] | `jitOptionsValues` | JIT options values, CUDA only |
| [in] | `numJitOptions` | Number of JIT options |
| [in] | `libraryOptions` | Library options |
| [in] | `libraryOptionValues` | Library options values |
| [in] | `numLibraryOptions` | Number of library options |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga5dff638bef38052c410ef3fa06fa1795)
