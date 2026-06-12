---
name: hip-hipgraphnodesetenabled
description: "Enables or disables the specified node in the given graphExec."
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

# hipGraphNodeSetEnabled

Enables or disables the specified node in the given graphExec.

## Signature

```c
hipError_t hipGraphNodeSetEnabled(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, unsigned int isEnabled);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - The executable graph in which to set the specified node. |
| [in] | `hNode` | - Node from the graph from which graphExec was instantiated. |
| [in] | `isEnabled` | - Node is enabled if != 0, otherwise the node is disabled. |

## Returns

hipSuccess , hipErrorInvalidValue ,

## Notes

- Sets hNode to be either enabled or disabled. Disabled nodes are functionally equivalent to empty nodes until they are reenabled. Existing node parameters are not affected by disabling/enabling the node.
- The node is identified by the corresponding hNode in the non-executable graph, from which the executable graph was instantiated.
- hNode must not have been removed from the original graph.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga8902200d9fed1df7644fc7a51c4d327b)
