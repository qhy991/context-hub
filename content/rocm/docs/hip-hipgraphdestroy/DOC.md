---
name: hip-hipgraphdestroy
description: "Destroys a graph."
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

# hipGraphDestroy

Destroys a graph.

## Signature

```c
hipError_t hipGraphDestroy(hipGraph_t graph);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - instance of graph to destroy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gadf21ff5ddbe98084e0fe3db592290ca7)
