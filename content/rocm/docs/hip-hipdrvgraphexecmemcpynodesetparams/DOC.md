---
name: hip-hipdrvgraphexecmemcpynodesetparams
description: "Sets the parameters for a memcpy node in the given graphExec."
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

# hipDrvGraphExecMemcpyNodeSetParams

Sets the parameters for a memcpy node in the given graphExec.

## Signature

```c
hipError_t hipDrvGraphExecMemcpyNodeSetParams(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, const HIP_MEMCPY3D *copyParams, hipCtx_t ctx);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - instance of the executable graph with the node. |
| [in] | `hNode` | - instance of the node to set parameters to. |
| [in] | `copyParams` | - const pointer to the memcpy node params. |
| [in] | `ctx` | - cotext related to current device. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga8173e6bad29de6ac5eab05463dda127c)
