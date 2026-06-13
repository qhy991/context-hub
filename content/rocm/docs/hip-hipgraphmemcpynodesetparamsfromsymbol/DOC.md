---
name: hip-hipgraphmemcpynodesetparamsfromsymbol
description: "Sets a memcpy node's parameters to copy from a symbol on the device."
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

# hipGraphMemcpyNodeSetParamsFromSymbol

Sets a memcpy node's parameters to copy from a symbol on the device.

## Signature

```c
hipError_t hipGraphMemcpyNodeSetParamsFromSymbol(hipGraphNode_t node, void *dst, const void *symbol, size_t count, size_t offset, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Instance of the node to set parameters of. |
| [in] | `dst` | - Pointer to memory address of the destination. |
| [in] | `symbol` | - Device symbol address. |
| [in] | `count` | - Size of the memory to copy. |
| [in] | `offset` | - Offset from start of symbol in bytes. |
| [in] | `kind` | - Type of memory copy. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga2d8fb8cff71140a7183b488dfd5c5642)
