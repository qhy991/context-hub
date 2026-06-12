---
name: hip-hipgraphbatchmemopnodesetparams
description: "Sets the batch mem op node's parameters.[BETA]."
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

# hipGraphBatchMemOpNodeSetParams

Sets the batch mem op node's parameters.[BETA].

## Signature

```c
hipError_t hipGraphBatchMemOpNodeSetParams(hipGraphNode_t hNode, hipBatchMemOpNodeParams *nodeParams);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hNode` | - Node to set the parameters for |
| [in] | `nodeParams` | - Parameters to copy |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Sets the parameters of batch mem op node hNode to nodeParams.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#gaec9d7d14e58a02bbd3dfe1f91cad8fcc)
