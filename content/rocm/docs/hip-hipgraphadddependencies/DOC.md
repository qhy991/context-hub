---
name: hip-hipgraphadddependencies
description: "Adds dependency edges to a graph."
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

# hipGraphAddDependencies

Adds dependency edges to a graph.

## Signature

```c
hipError_t hipGraphAddDependencies(hipGraph_t graph, const hipGraphNode_t *from, const hipGraphNode_t *to, size_t numDependencies);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - Instance of the graph to add dependencies to. |
| [in] | `from` | - Pointer to the graph nodes with dependencies to add from. |
| [in] | `to` | - Pointer to the graph nodes to add dependencies to. |
| [in] | `numDependencies` | - Number of dependencies to add. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga55de501ca624e30d33a58722b97ab119)
