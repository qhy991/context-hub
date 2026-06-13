---
name: hip-hipgraphexecmemcpynodesetparams
description: "Sets the parameters of a memcpy node in the given graphExec."
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

# hipGraphExecMemcpyNodeSetParams

Sets the parameters of a memcpy node in the given graphExec.

## Signature

```c
hipError_t hipGraphExecMemcpyNodeSetParams(hipGraphExec_t hGraphExec, hipGraphNode_t node, hipMemcpy3DParms *pNodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - Instance of the executable graph with the node. |
| [in] | `node` | - Instance of the node to set parameters of. |
| [in] | `pNodeParams` | - const pointer to the kernel node parameters. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga8b2a9b3158e565a1266269fed5f658ae)
