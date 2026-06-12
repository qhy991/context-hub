---
name: hip-hipgraphclone
description: "Clones a graph."
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

# hipGraphClone

Clones a graph.

## Signature

```c
hipError_t hipGraphClone(hipGraph_t *pGraphClone, hipGraph_t originalGraph);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pGraphClone` | - Returns newly created cloned graph. |
| [in] | `originalGraph` | - original graph to clone from. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorMemoryAllocation

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf9eec67b896029a35ee31055c247cc77)
