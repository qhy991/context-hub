---
name: hip-hipmodulegetglobal
description: "Returns a global pointer from a module."
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

# hipModuleGetGlobal

Returns a global pointer from a module.

## Signature

```c
hipError_t hipModuleGetGlobal(hipDeviceptr_t *dptr, size_t *bytes, hipModule_t hmod, const char *name);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dptr` | Returns global device pointer |
| [out] | `bytes` | Returns global size in bytes |
| [in] | `hmod` | Module to retrieve global from |
| [in] | `name` | Name of global to retrieve |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotFound , hipErrorInvalidContext

## Notes

- Returns in *dptr and *bytes the pointer and size of the global of name name located in module hmod. If no variable of that name exists, it returns hipErrorNotFound. Both parameters dptr and bytes are optional. If one of them is NULL, it is ignored and hipSuccess is returned.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga3e425a680285f495e776f096e9632c89)
