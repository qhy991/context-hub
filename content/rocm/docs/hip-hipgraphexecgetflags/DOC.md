---
name: hip-hipgraphexecgetflags
description: "Return the flags of an executable graph."
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

# hipGraphExecGetFlags

Return the flags of an executable graph.

## Signature

```c
hipError_t hipGraphExecGetFlags(hipGraphExec_t graphExec, unsigned long long *flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graphExec` | - Executable graph to get the flags from. |
| [out] | `flags` | - Flags used to instantiate this executable graph. |

## Returns

hipSuccess , hipErrorInvalidValue .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga87384379d402af7a44f1464419f65d46)
