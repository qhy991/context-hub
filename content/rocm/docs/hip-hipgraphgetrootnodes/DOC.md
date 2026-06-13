---
name: hip-hipgraphgetrootnodes
description: "Returns a graph's root nodes."
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

# hipGraphGetRootNodes

Returns a graph's root nodes.

## Signature

```c
hipError_t hipGraphGetRootNodes(hipGraph_t graph, hipGraphNode_t *pRootNodes, size_t *pNumRootNodes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - Instance of the graph to get the nodes from. |
| [out] | `pRootNodes` | - Pointer to return the graph's root nodes. |
| [out] | `pNumRootNodes` | - Returns the number of graph's root nodes. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- pRootNodes may be NULL, in which case this function will return the number of root nodes in pNumRootNodes. Otherwise, pNumRootNodes entries will be filled in. If pNumRootNodes is higher than the actual number of root nodes, the remaining entries in pRootNodes will be set to NULL, and the number of nodes actually obtained will be returned in pNumRootNodes.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gafc3f79160be0a919644835388258bd87)
