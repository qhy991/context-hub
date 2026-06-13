---
name: hip-hipgraphexecnodesetparams
description: "Updates parameters of an executable graph's node."
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

# hipGraphExecNodeSetParams

Updates parameters of an executable graph's node.

## Signature

```c
hipError_t hipGraphExecNodeSetParams(hipGraphExec_t graphExec, hipGraphNode_t node, hipGraphNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graphExec` | - Instance of the executable graph. |
| [in] | `node` | - Instance of the node to set parameters to. |
| [in] | `nodeParams` | - Pointer to the parameters to be set. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDeviceFunction , hipErrorNotSupported .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga8bc17629df369e20c61f8fba26b59a23)
