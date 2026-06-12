---
name: hip-hipgraphkernelnodecopyattributes
description: "Copies attributes from source node to destination node."
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

# hipGraphKernelNodeCopyAttributes

Copies attributes from source node to destination node.

## Signature

```c
hipError_t hipGraphKernelNodeCopyAttributes(hipGraphNode_t hSrc, hipGraphNode_t hDst);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `hDst` | - Destination node. |
| [in] | `hSrc` | - Source node. For list of attributes see hipKernelNodeAttrID . |

## Returns

hipSuccess , hipErrorInvalidContext

## Notes

- Copies attributes from source node to destination node. Both node must have the same context.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga6fd9af1ec50bc34c6500fe276d05946f)
