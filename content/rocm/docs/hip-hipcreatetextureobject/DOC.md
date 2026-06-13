---
name: hip-hipcreatetextureobject
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

# hipCreateTextureObject

Creates a texture object.

## Signature

```c
hipError_t hipCreateTextureObject(hipTextureObject_t *pTexObject, const hipResourceDesc *pResDesc, const hipTextureDesc *pTexDesc, const struct hipResourceViewDesc *pResViewDesc);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pTexObject` | pointer to the texture object to create |
| [in] | `pResDesc` | pointer to resource descriptor |
| [in] | `pTexDesc` | pointer to texture descriptor |
| [in] | `pResViewDesc` | pointer to resource view descriptor |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported , hipErrorOutOfMemory

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga8118c199ca3f347b5b5fd919bb624801)
