---
name: hip-hipgraphicsunmapresources
description: "Unmaps graphics resources."
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

# hipGraphicsUnmapResources

Unmaps graphics resources.

## Signature

```c
hipError_t hipGraphicsUnmapResources(int count, hipGraphicsResource_t *resources, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `count` | - Number of resources to unmap. |
| [in] | `resources` | - Pointer of resources to unmap. |
| [in] | `stream` | - Stream for synchronization. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorUnknown , hipErrorContextIsDestroyed

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graphics_interop.html#ga6a14e77207a54c59dea731345e3e6e72)
