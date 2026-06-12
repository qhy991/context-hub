---
name: hip-hipgraphexecupdateresult
description: "Enumeration type for GraphExecUpdateResult."
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

# hipGraphExecUpdateResult

Enumeration type for GraphExecUpdateResult.

## Type

Enum. typedef enum hipGraphExecUpdateResult {

## Values

`hipGraphExecUpdateSuccess`, `hipGraphExecUpdateError`, `hipGraphExecUpdateErrorTopologyChanged`, `hipGraphExecUpdateErrorNodeTypeChanged`, `hipGraphExecUpdateErrorFunctionChanged`, `hipGraphExecUpdateErrorParametersChanged`, `hipGraphExecUpdateErrorNotSupported`, `hipGraphExecUpdateErrorUnsupportedFunctionChange`

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gac79a2b2c0f83ae81c9325978c044892e)
