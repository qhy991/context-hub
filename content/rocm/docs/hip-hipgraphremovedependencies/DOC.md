---
name: hip-hipgraphremovedependencies
description: "Removes dependency edges from a graph."
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

# hipGraphRemoveDependencies

Removes dependency edges from a graph.

## Signature

```c
hipError_t hipGraphRemoveDependencies(hipGraph_t graph, const hipGraphNode_t *from, const hipGraphNode_t *to, size_t numDependencies);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - Instance of the graph to remove dependencies from. |
| [in] | `from` | - Array of nodes that provide the dependencies. |
| [in] | `to` | - Array of dependent nodes. |
| [in] | `numDependencies` | - Number of dependencies to remove. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga3a97f18f0c27e7cd58b404532e940dc6)
