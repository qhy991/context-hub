---
name: hip-hipgraphnodetype
description: "Enumeration type for GraphNodeType."
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

# hipGraphNodeType

Enumeration type for GraphNodeType.

## Type

Enum. typedef enum hipGraphNodeType {

## Values

`hipGraphNodeTypeKernel`, `hipGraphNodeTypeMemcpy`, `hipGraphNodeTypeMemset`, `hipGraphNodeTypeHost`, `hipGraphNodeTypeGraph`, `hipGraphNodeTypeEmpty`, `hipGraphNodeTypeWaitEvent`, `hipGraphNodeTypeEventRecord`, `hipGraphNodeTypeMemcpy1D`, `hipGraphNodeTypeMemcpyFromSymbol`, `hipGraphNodeTypeMemcpyToSymbol`

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga4727d20b89566832c74b762f987b9728)
