---
name: hip-hiptexobjectdestroy
description: "Destroys a texture object."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,texture-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Texture Management
---

# hipTexObjectDestroy

Destroys a texture object.

## Signature

```c
hipError_t hipTexObjectDestroy(hipTextureObject_t texObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `texObject` | texture object to destroy |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga9df0487a59efcdb063feecb770fa56c2)
