---
name: hip-hipgraphexeceventwaitnodesetevent
description: "Sets the event for an event record node in the given graphExec."
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

# hipGraphExecEventWaitNodeSetEvent

Sets the event for an event record node in the given graphExec.

## Signature

```c
hipError_t hipGraphExecEventWaitNodeSetEvent(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - instance of the executable graph with the node. |
| [in] | `hNode` | - node from the graph which was used to instantiate graphExec. |
| [in] | `event` | - pointer to the event. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gab7649d14c214d61f24e143c1599be9f0)
