---
name: hip-hipgrapheventrecordnodesetevent
description: "Sets an event record node's event."
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

# hipGraphEventRecordNodeSetEvent

Sets an event record node's event.

## Signature

```c
hipError_t hipGraphEventRecordNodeSetEvent(hipGraphNode_t node, hipEvent_t event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Instance of the node to set event to. |
| [in] | `event` | - Pointer to the event. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gac91ec8eb7a374eb1f7cec45e172efe8c)
