---
name: hip-hiptexobjectgetresourceviewdesc
description: "Gets resource view descriptor of a texture object."
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

# hipTexObjectGetResourceViewDesc

Gets resource view descriptor of a texture object.

## Signature

```c
hipError_t hipTexObjectGetResourceViewDesc(HIP_RESOURCE_VIEW_DESC *pResViewDesc, hipTextureObject_t texObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pResViewDesc` | pointer to resource view descriptor |
| [in] | `texObject` | texture object |

## Returns

hipSuccess , hipErrorNotSupported , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gac7b4b7bc09c32e2f2e25dbba07876a32)
