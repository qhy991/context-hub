---
name: hip-hipgraphnodefindinclone
description: "Finds a cloned version of a node."
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

# hipGraphNodeFindInClone

Finds a cloned version of a node.

## Signature

```c
hipError_t hipGraphNodeFindInClone(hipGraphNode_t *pNode, hipGraphNode_t originalNode, hipGraph_t clonedGraph);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pNode` | - Returns the cloned node. |
| [in] | `originalNode` | - original node handle. |
| [in] | `clonedGraph` | - Cloned graph to query. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga14d9f4cc7967a4cb06aca0631025495d)
