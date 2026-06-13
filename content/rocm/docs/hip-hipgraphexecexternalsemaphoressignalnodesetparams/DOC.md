---
name: hip-hipgraphexecexternalsemaphoressignalnodesetparams
description: "Updates node parameters in the external semaphore signal node in the given graphExec."
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

# hipGraphExecExternalSemaphoresSignalNodeSetParams

Updates node parameters in the external semaphore signal node in the given graphExec.

## Signature

```c
hipError_t hipGraphExecExternalSemaphoresSignalNodeSetParams(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, const hipExternalSemaphoreSignalNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - The executable graph in which to set the specified node. |
| [in] | `hNode` | - Node from the graph from which graphExec was instantiated. |
| [in] | `nodeParams` | - Pointer to the params to be set. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga69757fcf41c1939bb698f3e31913803b)
