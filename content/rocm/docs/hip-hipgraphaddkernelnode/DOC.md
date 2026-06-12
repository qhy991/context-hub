---
name: hip-hipgraphaddkernelnode
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

# hipGraphAddKernelNode

Creates a kernel execution node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddKernelNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, const hipKernelNodeParams *pNodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - Pointer to the dependencies of the kernel execution node. |
| [in] | `numDependencies` | - The number of the dependencies. |
| [in] | `pNodeParams` | - Pointer to the parameters of the kernel execution node. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDeviceFunction

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gab5d1eebec77853325f9f9884698b1a67)
