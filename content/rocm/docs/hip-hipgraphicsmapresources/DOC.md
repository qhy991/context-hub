---
name: hip-hipgraphicsmapresources
description: "Maps a graphics resource for access."
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

# hipGraphicsMapResources

Maps a graphics resource for access.

## Signature

```c
hipError_t hipGraphicsMapResources(int count, hipGraphicsResource_t *resources, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `count` | - Number of resources to map. |
| [in] | `resources` | - Pointer of resources to map. |
| [in] | `stream` | - Stream for synchronization. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorUnknown , hipErrorInvalidResourceHandle

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graphics_interop.html#gac625a73bf06d50c6554c08cb28e63aa6)
