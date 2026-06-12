---
name: hip-hipmoduleload
description: "Loads code object from file into a module the currrent context."
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

# hipModuleLoad

Loads code object from file into a module the currrent context.

## Signature

```c
hipError_t hipModuleLoad(hipModule_t *module, const char *fname);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `fname` | Filename of code object to load |
| [out] | `module` | Module |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidContext , hipErrorFileNotFound , hipErrorOutOfMemory , hipErrorSharedObjectInitFailed , hipErrorNotInitialized

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga31d806d976e91d36bd990ae3004d8760)
