---
name: hip-hipgraphicsunregisterresource
description: "Unregisters a graphics resource."
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

# hipGraphicsUnregisterResource

Unregisters a graphics resource.

## Signature

```c
hipError_t hipGraphicsUnregisterResource(hipGraphicsResource_t resource);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `resource` | - Graphics resources to unregister. |

## Returns

hipSuccess

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graphics_interop.html#ga48344c780768da2002fcfe3395c6a0c0)
