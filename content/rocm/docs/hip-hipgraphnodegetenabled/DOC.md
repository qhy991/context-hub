---
name: hip-hipgraphnodegetenabled
description: "Query whether a node in the given graphExec is enabled."
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

# hipGraphNodeGetEnabled

Query whether a node in the given graphExec is enabled.

## Signature

```c
hipError_t hipGraphNodeGetEnabled(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, unsigned int *isEnabled);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - The executable graph in which to set the specified node. |
| [in] | `hNode` | - Node from the graph from which graphExec was instantiated. |
| [out] | `isEnabled` | - Location to return the enabled status of the node. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Sets isEnabled to 1 if hNode is enabled, or 0 if it is disabled.
- The node is identified by the corresponding node in the non-executable graph, from which the executable graph was instantiated.
- hNode must not have been removed from the original graph.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga207d60e261a723f81dd573423602239c)
