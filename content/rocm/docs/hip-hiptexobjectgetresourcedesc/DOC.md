---
name: hip-hiptexobjectgetresourcedesc
description: "Gets resource descriptor of a texture object."
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
  hw_unit: driver
  api_module: Texture Management
---

# hipTexObjectGetResourceDesc

Gets resource descriptor of a texture object.

## Signature

```c
hipError_t hipTexObjectGetResourceDesc(HIP_RESOURCE_DESC *pResDesc, hipTextureObject_t texObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pResDesc` | pointer to resource descriptor |
| [in] | `texObject` | texture object |

## Returns

hipSuccess , hipErrorNotSupported , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gac136126d65935da5ca274ac628aa67a4)
