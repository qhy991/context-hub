---
name: hip-hipgraphaddmemcpynode
description: "Creates a memcpy node and adds it to a graph."
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

# hipGraphAddMemcpyNode

Creates a memcpy node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemcpyNode(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, const hipMemcpy3DParms *pCopyParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created. |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - const pointer to the dependencies of the memcpy execution node. |
| [in] | `numDependencies` | - The number of dependencies. |
| [in] | `pCopyParams` | - const pointer to the parameters for the memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gafc4759560bef7b96ca3eefccde8dd550)
