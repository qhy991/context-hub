---
name: hip-hiptexobjectcreate
description: "Creates a texture object."
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

# hipTexObjectCreate

Creates a texture object.

## Signature

```c
hipError_t hipTexObjectCreate(hipTextureObject_t *pTexObject, const HIP_RESOURCE_DESC *pResDesc, const HIP_TEXTURE_DESC *pTexDesc, const HIP_RESOURCE_VIEW_DESC *pResViewDesc);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pTexObject` | pointer to texture object to create |
| [in] | `pResDesc` | pointer to resource descriptor |
| [in] | `pTexDesc` | pointer to texture descriptor |
| [in] | `pResViewDesc` | pointer to resource view descriptor |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga59d6d76f9ea1e4f58eb3b86958ae1ee4)
