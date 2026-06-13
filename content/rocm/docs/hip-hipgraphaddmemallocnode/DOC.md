---
name: hip-hipgraphaddmemallocnode
description: "Creates a memory allocation node and adds it to a graph."
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

# hipGraphAddMemAllocNode

Creates a memory allocation node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemAllocNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, hipMemAllocNodeParams *pNodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to the graph node to create and add to the graph |
| [in] | `graph` | - Instance of the graph node to be added |
| [in] | `pDependencies` | - Const pointer to the node dependencies |
| [in] | `numDependencies` | - The number of dependencies |
| [in,out] | `pNodeParams` | - Node parameters for memory allocation, returns a pointer to the allocated memory. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gae9ea0d05ebde492309f77ba0a23b81a9)
