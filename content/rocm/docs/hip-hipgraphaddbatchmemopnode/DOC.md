---
name: hip-hipgraphaddbatchmemopnode
description: "Creates a batch memory operation node and adds it to a graph.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-memory-operations
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Memory Operations
---

# hipGraphAddBatchMemOpNode

Creates a batch memory operation node and adds it to a graph.[BETA].

## Signature

```c
hipError_t hipGraphAddBatchMemOpNode(hipGraphNode_t *phGraphNode, hipGraph_t hGraph, const hipGraphNode_t *dependencies, size_t numDependencies, const hipBatchMemOpNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `phGraphNode` | - Returns the newly created node |
| [in] | `hGraph` | - Graph to which to add the node |
| [in] | `dependencies` | - Dependencies of the node |
| [in] | `numDependencies` | - Number of dependencies |
| [in] | `nodeParams` | - Parameters for the node |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#ga6860128392dad469e80896d615063900)
