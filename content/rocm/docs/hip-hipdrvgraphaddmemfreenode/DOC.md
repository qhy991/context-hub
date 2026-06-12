---
name: hip-hipdrvgraphaddmemfreenode
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
  hw_unit: driver
  api_module: Graph Management
---

# hipDrvGraphAddMemFreeNode

Creates a memory free node and adds it to a graph.

## Signature

```c
hipError_t hipDrvGraphAddMemFreeNode(hipGraphNode_t *phGraphNode, hipGraph_t hGraph, const hipGraphNode_t *dependencies, size_t numDependencies, hipDeviceptr_t dptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `phGraphNode` | - Pointer to the graph node to create and add to the graph |
| [in] | `hGraph` | - Instance of the graph the node to be added |
| [in] | `dependencies` | - Const pointer to the node dependencies |
| [in] | `numDependencies` | - The number of dependencies |
| [in] | `dptr` | - Pointer to the memory to be freed |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga55f78947cfc9b1844672f11d197ddeed)
