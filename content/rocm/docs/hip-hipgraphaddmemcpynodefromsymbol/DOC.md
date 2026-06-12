---
name: hip-hipgraphaddmemcpynodefromsymbol
description: "Creates a memcpy node to copy from a symbol on the device and adds it to a graph."
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

# hipGraphAddMemcpyNodeFromSymbol

Creates a memcpy node to copy from a symbol on the device and adds it to a graph.

## Signature

```c
hipError_t hipGraphAddMemcpyNodeFromSymbol(hipGraphNode_t *pGraphNode, hipGraph_t graph, const hipGraphNode_t *pDependencies, size_t numDependencies, void *dst, const void *symbol, size_t count, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphNode` | - Pointer to graph node that is created. |
| [in] | `graph` | - Instance of graph to add the created node to. |
| [in] | `pDependencies` | - const pointer to the dependencies of the memcpy execution node. |
| [in] | `numDependencies` | - Number of the dependencies. |
| [in] | `dst` | - Pointer to memory address of the destination. |
| [in] | `symbol` | - Device symbol address. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `offset` | - Offset from start of symbol in bytes. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga6f3c6ac9b90264dd297f9ee45fdb5a1c)
