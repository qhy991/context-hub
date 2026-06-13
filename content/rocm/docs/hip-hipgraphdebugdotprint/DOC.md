---
name: hip-hipgraphdebugdotprint
description: "Write a DOT file describing graph structure."
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

# hipGraphDebugDotPrint

Write a DOT file describing graph structure.

## Signature

```c
hipError_t hipGraphDebugDotPrint(hipGraph_t graph, const char *path, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - graph object for which DOT file has to be generated. |
| [in] | `path` | - path to write the DOT file. |
| [in] | `flags` | - Flags from hipGraphDebugDotFlags to get additional node information. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorOperatingSystem

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaad520a916f418e08e0ca9078a21e244f)
