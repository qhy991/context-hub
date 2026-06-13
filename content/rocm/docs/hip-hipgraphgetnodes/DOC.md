---
name: hip-hipgraphgetnodes
description: "Returns a graph's nodes."
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

# hipGraphGetNodes

Returns a graph's nodes.

## Signature

```c
hipError_t hipGraphGetNodes(hipGraph_t graph, hipGraphNode_t *nodes, size_t *numNodes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - Instance of graph to get the nodes from. |
| [out] | `nodes` | - Pointer to return the graph nodes. |
| [out] | `numNodes` | - Returns the number of graph nodes. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- nodes may be NULL, in which case this function will return the number of nodes in numNodes. Otherwise, numNodes entries will be filled in. If numNodes is higher than the actual number of nodes, the remaining entries in nodes will be set to NULL, and the number of nodes actually obtained will be returned in numNodes.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf006701d98164ed3492755bbb19bab83)
