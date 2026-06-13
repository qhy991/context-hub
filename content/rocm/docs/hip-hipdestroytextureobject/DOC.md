---
name: hip-hipdestroytextureobject
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

# hipDestroyTextureObject

Destroys a texture object.

## Signature

```c
hipError_t hipDestroyTextureObject(hipTextureObject_t textureObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `textureObject` | texture object to destroy |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gad62c874fe1ae049c9e93a83623b3a82f)
