---
name: hip-hipdrvgraphaddmemcpynode
description: "Creates a memcpy node and adds it to a graph."
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

# hipDrvGraphAddMemcpyNode

Creates a memcpy node and adds it to a graph.

## Signature

```c
hipError_t hipDrvGraphAddMemcpyNode(hipGraphNode_t *phGraphNode, hipGraph_t hGraph, const hipGraphNode_t *dependencies, size_t numDependencies, const HIP_MEMCPY3D *copyParams, hipCtx_t ctx);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `phGraphNode` | - Pointer to graph node that is created. |
| [in] | `hGraph` | - Instance of graph to add the created node to. |
| [in] | `dependencies` | - const pointer to the dependencies of the memcpy execution node. |
| [in] | `numDependencies` | - The number of dependencies. |
| [in] | `copyParams` | - const pointer to the parameters for the memory copy. |
| [in] | `ctx` | - context related to current device. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga33aff03ac42d5ccf4bc39d78b91d1397)
