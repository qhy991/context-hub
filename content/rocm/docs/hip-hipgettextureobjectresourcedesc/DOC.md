---
name: hip-hipgettextureobjectresourcedesc
description: "Gets resource descriptor for the texture object."
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

# hipGetTextureObjectResourceDesc

Gets resource descriptor for the texture object.

## Signature

```c
hipError_t hipGetTextureObjectResourceDesc(hipResourceDesc *pResDesc, hipTextureObject_t textureObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pResDesc` | pointer to resource descriptor |
| [in] | `textureObject` | texture object |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga5eb7e8f8a486500243cb43b0a3d11d06)
