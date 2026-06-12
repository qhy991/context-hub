---
name: hip-hipgraphexternalsemaphoreswaitnodegetparams
description: "Returns external semaphore wait node params."
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

# hipGraphExternalSemaphoresWaitNodeGetParams

Returns external semaphore wait node params.

## Signature

```c
hipError_t hipGraphExternalSemaphoresWaitNodeGetParams(hipGraphNode_t hNode, hipExternalSemaphoreWaitNodeParams *params_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hNode` | - Node from the graph from which graphExec was instantiated. |
| [out] | `params_out` | - Pointer to params. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf6e73d6a19ca850f395febf4adb46ce7)
