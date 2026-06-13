---
name: hip-hipgraphcreate
description: "Creates a graph."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Graph Management
---

# hipGraphCreate

Creates a graph.

## Signature

```c
hipError_t hipGraphCreate(hipGraph_t *pGraph, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraph` | - pointer to graph to create. |
| [in] | `flags` | - flags for graph creation, must be 0. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorMemoryAllocation

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga0569a00583e14be02790df5531e905d6)
