---
name: hip-hipgraphicsresourcegetmappedpointer
description: "Gets device accessible address of a graphics resource."
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

# hipGraphicsResourceGetMappedPointer

Gets device accessible address of a graphics resource.

## Signature

```c
hipError_t hipGraphicsResourceGetMappedPointer(void ** devPtr , size_t * size , hipGraphicsResource_t resource);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `devPtr` | - Pointer of device through which graphic resource may be accessed. |
| [out] | `size` | - Size of the buffer accessible from devPtr. |
| [in] | `resource` | - Mapped resource to access. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graphics_interop.html#gac06c5fe793213a7cc4047c2ae42fd915)
