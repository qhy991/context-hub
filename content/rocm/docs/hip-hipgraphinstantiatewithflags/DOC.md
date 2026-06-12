---
name: hip-hipgraphinstantiatewithflags
description: "Creates an executable graph from a graph."
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

# hipGraphInstantiateWithFlags

Creates an executable graph from a graph.

## Signature

```c
hipError_t hipGraphInstantiateWithFlags(hipGraphExec_t *pGraphExec, hipGraph_t graph, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphExec` | - Pointer to instantiated executable graph. |
| [in] | `graph` | - Instance of graph to instantiate. |
| [in] | `flags` | - Flags to control instantiation. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga5f8c8f7c3cf2db57908891b715759028)
