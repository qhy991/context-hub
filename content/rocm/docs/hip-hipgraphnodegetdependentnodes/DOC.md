---
name: hip-hipgraphnodegetdependentnodes
description: "Returns a node's dependent nodes."
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

# hipGraphNodeGetDependentNodes

Returns a node's dependent nodes.

## Signature

```c
hipError_t hipGraphNodeGetDependentNodes(hipGraphNode_t node, hipGraphNode_t *pDependentNodes, size_t *pNumDependentNodes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Graph node to get the dependent nodes from. |
| [out] | `pDependentNodes` | - Pointer to return the graph dependent nodes. |
| [out] | `pNumDependentNodes` | - Returns the number of graph node dependent nodes. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- pDependentNodes may be NULL, in which case this function will return the number of dependent nodes in pNumDependentNodes. Otherwise, pNumDependentNodes entries will be filled in. If pNumDependentNodes is higher than the actual number of dependent nodes, the remaining entries in pDependentNodes will be set to NULL, and the number of nodes actually obtained will be returned in pNumDependentNodes.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga5ca0eedf026ec470d3e7d10724b08253)
