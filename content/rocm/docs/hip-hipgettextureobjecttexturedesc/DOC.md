---
name: hip-hipgettextureobjecttexturedesc
description: "Gets texture descriptor for the texture object."
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

# hipGetTextureObjectTextureDesc

Gets texture descriptor for the texture object.

## Signature

```c
hipError_t hipGetTextureObjectTextureDesc(hipTextureDesc *pTexDesc, hipTextureObject_t textureObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pTexDesc` | pointer to texture descriptor |
| [in] | `textureObject` | texture object |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gaf14cf44212e7191a2553d4d09e4fd665)
