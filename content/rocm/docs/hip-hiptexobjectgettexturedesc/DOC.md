---
name: hip-hiptexobjectgettexturedesc
description: "Gets texture descriptor of a texture object."
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

# hipTexObjectGetTextureDesc

Gets texture descriptor of a texture object.

## Signature

```c
hipError_t hipTexObjectGetTextureDesc(HIP_TEXTURE_DESC *pTexDesc, hipTextureObject_t texObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pTexDesc` | pointer to texture descriptor |
| [in] | `texObject` | texture object |

## Returns

hipSuccess , hipErrorNotSupported , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga7d65d4114af2b8ccc803a3bd7f40badd)
