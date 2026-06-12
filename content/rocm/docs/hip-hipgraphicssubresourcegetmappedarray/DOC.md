---
name: hip-hipgraphicssubresourcegetmappedarray
description: "Get an array through which to access a subresource of a mapped graphics resource."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,graphics-interoperability
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Graphics Interoperability
---

# hipGraphicsSubResourceGetMappedArray

Get an array through which to access a subresource of a mapped graphics resource.

## Signature

```c
hipError_t hipGraphicsSubResourceGetMappedArray(hipArray_t * array , hipGraphicsResource_t resource, unsigned int arrayIndex, unsigned int mipLevel);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `array` | - Pointer of array through which a subresource of resource may be accessed. |
| [in] | `resource` | - Mapped resource to access. |
| [in] | `arrayIndex` | - Array index for the subresource to access. |
| [in] | `mipLevel` | - Mipmap level for the subresource to access. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graphics_interop.html#ga9051a8bc901816be265c5de8f2202775)
