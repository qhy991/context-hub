---
name: hip-hipgraphinstantiatewithparams
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
  symbol_kind: function
  hw_unit: driver
  api_module: Graph Management
---

# hipGraphInstantiateWithParams

Creates an executable graph from a graph.

## Signature

```c
hipError_t hipGraphInstantiateWithParams(hipGraphExec_t *pGraphExec, hipGraph_t graph, hipGraphInstantiateParams *instantiateParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphExec` | - Pointer to instantiated executable graph. |
| [in] | `graph` | - Instance of graph to instantiate. |
| [in] | `instantiateParams` | - Graph instantiation Params |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga97772b87ae4396a8100890df46890c8c)
