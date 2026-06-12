---
name: hip-hipgraphaddmemcpynode1d
description: "Creates a 1D memcpy node and adds it to a graph."
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

# hipGraphAddMemcpyNode1D

Creates a 1D memcpy node and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemcpyNode1D(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, void *dst, const void *src, size_t count, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created. |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - const pointer to the dependencies of the memcpy execution node. |
| [in] | `numDependencies` | - The number of dependencies. |
| [in] | `dst` | - Pointer to memory address of the destination. |
| [in] | `src` | - Pointer to memory address of the source. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga05e51a4f490804536f16f5dc83459ca1)
