---
name: hip-hipgettextureobjectresourceviewdesc
description: "Gets resource view descriptor for the texture object."
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

# hipGetTextureObjectResourceViewDesc

Gets resource view descriptor for the texture object.

## Signature

```c
hipError_t hipGetTextureObjectResourceViewDesc(struct hipResourceViewDesc *pResViewDesc, hipTextureObject_t textureObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pResViewDesc` | pointer to resource view descriptor |
| [in] | `textureObject` | texture object |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga748e53ac1b10eb11d41efab0de154966)
