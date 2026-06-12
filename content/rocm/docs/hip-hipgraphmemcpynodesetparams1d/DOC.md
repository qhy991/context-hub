---
name: hip-hipgraphmemcpynodesetparams1d
description: "Sets a memcpy node's parameters to perform a 1-dimensional copy."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,graph-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Graph Management
---

# hipGraphMemcpyNodeSetParams1D

Sets a memcpy node's parameters to perform a 1-dimensional copy.

## Signature

```c
hipError_t hipGraphMemcpyNodeSetParams1D(hipGraphNode_t node, void *dst, const void *src, size_t count, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Instance of the node to set parameters of. |
| [in] | `dst` | - Pointer to memory address of the destination. |
| [in] | `src` | - Pointer to memory address of the source. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga3c7686dca4a405d9ec5a8a89615d33a7)
