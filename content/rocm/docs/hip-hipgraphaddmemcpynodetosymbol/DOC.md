---
name: hip-hipgraphaddmemcpynodetosymbol
description: "Creates a memcpy node to copy to a symbol on the device and adds it to a graph."
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

# hipGraphAddMemcpyNodeToSymbol

Creates a memcpy node to copy to a symbol on the device and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemcpyNodeToSymbol(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, const void *symbol, const void *src, size_t count, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created. |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - const pointer to the dependencies on the memcpy execution node. |
| [in] | `numDependencies` | - Number of dependencies. |
| [in] | `symbol` | - Device symbol address. |
| [in] | `src` | - Pointer to memory address of the src. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `offset` | - Offset from start of symbol in bytes. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gadc76882339279fa8c70f9666d2088435)
