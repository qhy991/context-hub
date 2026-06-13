---
name: hip-hipgraphmemfreenodegetparams
description: "Returns parameters for memory free node."
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

# hipGraphMemFreeNodeGetParams

Returns parameters for memory free node.

## Signature

```c
hipError_t hipGraphMemFreeNodeGetParams(hipGraphNode_t node, void *dev_ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Memory free node to query |
| [out] | `dev_ptr` | - Device pointer of the specified memory free node |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga0173b789bbf238185d90733fe36d9a07)
