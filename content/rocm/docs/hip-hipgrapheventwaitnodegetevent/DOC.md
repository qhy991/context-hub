---
name: hip-hipgrapheventwaitnodegetevent
description: "Returns the event associated with an event wait node."
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

# hipGraphEventWaitNodeGetEvent

Returns the event associated with an event wait node.

## Signature

```c
hipError_t hipGraphEventWaitNodeGetEvent(hipGraphNode_t node, hipEvent_t *event_out);
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
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaccfa3e841e4af4a1897b52f47d75a43d)
