---
name: hip-hipdestroysurfaceobject
description: "Destroy a surface object."
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

# hipDestroySurfaceObject

Destroy a surface object.

## Signature

```c
hipError_t hipDestroySurfaceObject(hipSurfaceObject_t surfaceObject);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `surfaceObject` | Surface object to be destroyed. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___surface.html#ga1cbf692fdb56b251d7b6d4e4d3bb2006)
