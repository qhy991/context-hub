---
name: hip-hipmoduleunload
description: "Frees the module."
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

# hipModuleUnload

Frees the module.

## Signature

```c
hipError_t hipModuleUnload(hipModule_t module);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `module` | Module to free |

## Returns

hipSuccess , hipErrorInvalidResourceHandle

## Notes

- The module is freed, and the code objects associated with it are destroyed.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gae58e345f55bb3ec13dca80d2df88e0ed)
