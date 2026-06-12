---
name: hip-hipgraphbatchmemopnodegetparams
description: "Returns a batch mem op node's parameters.[BETA]."
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

# hipGraphBatchMemOpNodeGetParams

Returns a batch mem op node's parameters.[BETA].

## Signature

```c
hipError_t hipGraphBatchMemOpNodeGetParams(hipGraphNode_t hNode, hipBatchMemOpNodeParams *nodeParams_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hNode` | - Node to get the parameters for |
| [in] | `nodeParams_out` | - Pointer to return the parameters |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Returns the parameters of batch mem op node hNode in nodeParams_out. The paramArray returned in nodeParams_out is owned by the node. This memory remains valid until the node is destroyed or its parameters are modified, and should not be modified directly.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#gab6df0e565e2c5bae06975f3c9f6ea3a1)
