---
name: hip-hipgraphexecupdate
description: "Check whether an executable graph can be updated with a graph and perform the update if * possible."
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

# hipGraphExecUpdate

Check whether an executable graph can be updated with a graph and perform the update if * possible.

## Signature

```c
hipError_t hipGraphExecUpdate(hipGraphExec_t hGraphExec, hipGraph_t hGraph, hipGraphNode_t *hErrorNode_out, hipGraphExecUpdateResult *updateResult_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - instance of executable graph to update. |
| [in] | `hGraph` | - graph that contains the updated parameters. |
| [in] | `hErrorNode_out` | - node which caused the permissibility check to forbid the update. |
| [in] | `updateResult_out` | - Return code whether the graph update was performed. |

## Returns

hipSuccess , hipErrorGraphExecUpdateFailure

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga0fb2ea2d5d6348888b074a7e44738b98)
