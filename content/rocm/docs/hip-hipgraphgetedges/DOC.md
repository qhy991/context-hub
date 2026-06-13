---
name: hip-hipgraphgetedges
description: "Returns a graph's dependency edges."
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

# hipGraphGetEdges

Returns a graph's dependency edges.

## Signature

```c
hipError_t hipGraphGetEdges(hipGraph_t graph, hipGraphNode_t *from, hipGraphNode_t *to, size_t *numEdges);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - Instance of the graph to get the edges from. |
| [out] | `from` | - Pointer to the graph nodes to return edge endpoints. |
| [out] | `to` | - Pointer to the graph nodes to return edge endpoints. |
| [out] | `numEdges` | - Returns number of edges. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- from and to may both be NULL, in which case this function only returns the number of edges in numEdges. Otherwise, numEdges entries will be filled in. If numEdges is higher than the actual number of edges, the remaining entries in from and to will be set to NULL, and the number of edges actually returned will be written to numEdges.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gab44fc541c62279d674436289d8f504b1)
