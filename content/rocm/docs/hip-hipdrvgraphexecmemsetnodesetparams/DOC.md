---
name: hip-hipdrvgraphexecmemsetnodesetparams
description: "Sets the parameters for a memset node in the given graphExec."
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

# hipDrvGraphExecMemsetNodeSetParams

Sets the parameters for a memset node in the given graphExec.

## Signature

```c
hipError_t hipDrvGraphExecMemsetNodeSetParams(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, const hipMemsetParams *memsetParams, hipCtx_t ctx);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - instance of the executable graph with the node. |
| [in] | `hNode` | - instance of the node to set parameters to. |
| [in] | `memsetParams` | - pointer to the parameters. |
| [in] | `ctx` | - cotext related to current device. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga037dcdd56f1ebe098380f2ba0b88e539)
