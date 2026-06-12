---
name: hip-hipgrapheventrecordnodegetevent
description: "Returns the event associated with an event record node."
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

# hipGraphEventRecordNodeGetEvent

Returns the event associated with an event record node.

## Signature

```c
hipError_t hipGraphEventRecordNodeGetEvent(hipGraphNode_t node, hipEvent_t *event_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Instance of the node to get event of. |
| [out] | `event_out` | - Pointer to return the event. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gad5cf984b5b764ca5d715a6673cc5d6cb)
