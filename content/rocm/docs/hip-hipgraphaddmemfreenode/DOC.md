---
name: hip-hipgraphaddmemfreenode
description: "Creates a memory free node and adds it to a graph."
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

# hipGraphAddMemFreeNode

Creates a memory free node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemFreeNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, void *dev_ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to the graph node to create and add to the graph |
| [in] | `graph` | - Instance of the graph node to be added |
| [in] | `pDependencies` | - Const pointer to the node dependencies |
| [in] | `numDependencies` | - The number of dependencies |
| [in] | `dev_ptr` | - Pointer to the memory to be freed |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga70f6f4924c404883cbc0d7cb6ac38100)
