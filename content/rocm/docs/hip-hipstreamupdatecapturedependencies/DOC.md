---
name: hip-hipstreamupdatecapturedependencies
description: "Update the set of dependencies in a capturing stream."
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

# hipStreamUpdateCaptureDependencies

Update the set of dependencies in a capturing stream.

## Signature

```c
hipError_t hipStreamUpdateCaptureDependencies(hipStream_t stream, hipGraphNode_t *dependencies, size_t numDependencies, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream that is being captured. |
| [in] | `dependencies` | Pointer to an array of nodes to add/replace. |
| [in] | `numDependencies` | Size of the dependencies array. |
| [in] | `flags` | Flag to update dependency set. Should be one of the values in enum hipStreamUpdateCaptureDependenciesFlags . |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorIllegalState

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf40ec47e46b07252d36204482ab47c02)
