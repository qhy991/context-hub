---
name: hip-hipgraphexecbatchmemopnodesetparams
description: "Sets the parameters for a batch mem op node in the given graphExec.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-memory-operations
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Stream Memory Operations
---

# hipGraphExecBatchMemOpNodeSetParams

Sets the parameters for a batch mem op node in the given graphExec.[BETA].

## Signature

```c
hipError_t hipGraphExecBatchMemOpNodeSetParams(hipGraphExec_t hGraphExec, hipGraphNode_t hNode, const hipBatchMemOpNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - The executable graph in which to set the specified node |
| [in] | `hNode` | - Batch mem op node from the graph from which graphExec was instantiated |
| [in] | `nodeParams` | - Updated Parameters to set |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Sets the parameters of a batch mem op node in an executable graph hGraphExec. The node is identified by the corresponding node hNode in the non-executable graph, from which the executable graph was instantiated.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#ga55131ad428510b022abd5c9b65634731)
