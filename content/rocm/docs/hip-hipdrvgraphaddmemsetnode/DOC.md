---
name: hip-hipdrvgraphaddmemsetnode
description: "Creates a memset node and adds it to a graph."
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

# hipDrvGraphAddMemsetNode

Creates a memset node and adds it to a graph.

## Signature

```c
hipError_t hipDrvGraphAddMemsetNode(hipGraphNode_t *phGraphNode, hipGraph_t hGraph, const hipGraphNode_t *dependencies, size_t numDependencies, const hipMemsetParams *memsetParams, hipCtx_t ctx);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `phGraphNode` | - pointer to graph node to create. |
| [in] | `hGraph` | - instance of graph to add the created node to. |
| [in] | `dependencies` | - const pointer to the dependencies on the memset execution node. |
| [in] | `numDependencies` | - number of the dependencies. |
| [in] | `memsetParams` | - const pointer to the parameters for the memory set. |
| [in] | `ctx` | - cotext related to current device. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga66548119eaa99f46d32073955239b2f2)
