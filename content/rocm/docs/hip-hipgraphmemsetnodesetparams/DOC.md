---
name: hip-hipgraphmemsetnodesetparams
description: "Sets a memset node's parameters."
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

# hipGraphMemsetNodeSetParams

Sets a memset node's parameters.

## Signature

```c
hipError_t hipGraphMemsetNodeSetParams(hipGraphNode_t node, const hipMemsetParams *pNodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Instance of the node to set parameters of. |
| [in] | `pNodeParams` | - Pointer to the parameters. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gad5ab6dd1f9d88c3bc662c271c8aff1a3)
