---
name: hip-hipgraphaddeventrecordnode
description: "Creates an event record node and adds it to a graph."
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

# hipGraphAddEventRecordNode

Creates an event record node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddEventRecordNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created. |
| [in] | `graph` | - Instance of the graph the node is added to. |
| [in] | `pDependencies` | - const pointer to the node dependencies. |
| [in] | `numDependencies` | - Number of dependencies. |
| [in] | `event` | - Event of the node. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga74dca46f970bafa279ec9af41ceca7a9)
