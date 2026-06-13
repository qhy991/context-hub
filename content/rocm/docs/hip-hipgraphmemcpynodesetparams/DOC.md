---
name: hip-hipgraphmemcpynodesetparams
description: "Sets a memcpy node's parameters."
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

# hipGraphMemcpyNodeSetParams

Sets a memcpy node's parameters.

## Signature

```c
hipError_t hipGraphMemcpyNodeSetParams(hipGraphNode_t node, const hipMemcpy3DParms *pNodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - instance of the node to set parameters to. |
| [in] | `pNodeParams` | - const pointer to the parameters. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga098c63fb0fbb57e8d9ee6da0fbfccc70)
