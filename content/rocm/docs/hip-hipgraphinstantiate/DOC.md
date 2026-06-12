---
name: hip-hipgraphinstantiate
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

# hipGraphInstantiate

Creates an executable graph from a graph.

## Signature

```c
hipError_t hipGraphInstantiate(hipGraphExec_t *pGraphExec, hipGraph_t graph, hipGraphNode_t *pErrorNode, char *pLogBuffer, size_t bufferSize);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphExec` | - Pointer to instantiated executable graph. |
| [in] | `graph` | - Instance of graph to instantiate. |
| [out] | `pErrorNode` | - Pointer to error node. In case an error occured during graph instantiation, it could modify the corresponding node. |
| [out] | `pLogBuffer` | - Pointer to log buffer. |
| [out] | `bufferSize` | - Size of the log buffer. |

## Returns

hipSuccess , hipErrorOutOfMemory

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf5ede92050539e795805f4e2705e6b59)
