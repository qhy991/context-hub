---
name: hip-hipgraphaddnode
description: "Creates a kernel execution node and adds it to a graph."
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

# hipGraphAddNode

Creates a kernel execution node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, hipGraphNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to kernel graph node that is created. |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - Pointer to the dependencies on the kernel execution node. |
| [in] | `numDependencies` | - Number of dependencies. |
| [in] | `nodeParams` | - Pointer to the node parameters. |

## Returns

hipSuccess , hipErrorInvalidValue .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaefab3caa775470618527796774eae6f9)
