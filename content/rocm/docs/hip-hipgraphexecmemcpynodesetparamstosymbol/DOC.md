---
name: hip-hipgraphexecmemcpynodesetparamstosymbol
description: "Sets the parameters for a memcpy node in the given graphExec to copy to a symbol on the device."
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

# hipGraphExecMemcpyNodeSetParamsToSymbol

Sets the parameters for a memcpy node in the given graphExec to copy to a symbol on the device.

## Signature

```c
hipError_t hipGraphExecMemcpyNodeSetParamsToSymbol(hipGraphExec_t hGraphExec, hipGraphNode_t node, const void *symbol, const void *src, size_t count, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hGraphExec` | - Instance of the executable graph with the node. |
| [in] | `node` | - Instance of the node to set parameters of. |
| [in] | `symbol` | - Device symbol address. |
| [in] | `src` | - Pointer to memory address of the src. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `offset` | - Offset from start of symbol in bytes. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga698fb0f0bd392e4f383ee62e9a61d1e0)
