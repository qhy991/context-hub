---
name: hip-hipmodulegettexref
description: "returns the handle of the texture reference with the name from the module."
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

# hipModuleGetTexRef

returns the handle of the texture reference with the name from the module.

## Signature

```c
hipError_t hipModuleGetTexRef(textureReference **texRef, hipModule_t hmod, const char *name);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hmod` | Module |
| [in] | `name` | Pointer of name of texture reference |
| [out] | `texRef` | Pointer of texture reference |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorNotFound , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga1ceb20d084d571c28282ee2fd052264c)
