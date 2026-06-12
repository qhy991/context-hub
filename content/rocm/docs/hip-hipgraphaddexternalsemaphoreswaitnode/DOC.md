---
name: hip-hipgraphaddexternalsemaphoreswaitnode
description: "Creates a external semaphor wait node and adds it to a graph."
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

# hipGraphAddExternalSemaphoresWaitNode

Creates a external semaphor wait node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddExternalSemaphoresWaitNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, const hipExternalSemaphoreWaitNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - pointer to the graph node to create. |
| [in] | `graph` | - instance of the graph to add the created node. |
| [in] | `pDependencies` | - const pointer to the dependencies on the memset execution node. |
| [in] | `numDependencies` | - the number of the dependencies. |
| [in] | `nodeParams` | -pointer to the parameters. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gac086da9e2ee7561a7b47ce4f7276faf2)
