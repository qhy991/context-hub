---
name: hip-hipcreatesurfaceobject
description: "Create a surface object."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,surface-object
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Surface Object
---

# hipCreateSurfaceObject

Create a surface object.

## Signature

```c
hipError_t hipCreateSurfaceObject(hipSurfaceObject_t *pSurfObject, const hipResourceDesc *pResDesc);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pSurfObject` | Pointer of surface object to be created. |
| [in] | `pResDesc` | Pointer of suface object descriptor. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___surface.html#gaa06a02200e471cedeed33b9d326e9dd6)
