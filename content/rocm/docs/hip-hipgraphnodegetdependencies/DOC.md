---
name: hip-hipgraphnodegetdependencies
description: "Returns a node's dependencies."
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

# hipGraphNodeGetDependencies

Returns a node's dependencies.

## Signature

```c
hipError_t hipGraphNodeGetDependencies(hipGraphNode_t node, hipGraphNode_t *pDependencies, size_t *pNumDependencies);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `node` | - Graph node to get the dependencies from. |
| [out] | `pDependencies` | - Pointer to return the dependencies. |
| [out] | `pNumDependencies` | - Returns the number of graph node dependencies. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- pDependencies may be NULL, in which case this function will return the number of dependencies in pNumDependencies. Otherwise, pNumDependencies entries will be filled in. If pNumDependencies is higher than the actual number of dependencies, the remaining entries in pDependencies will be set to NULL, and the number of nodes actually obtained will be returned in pNumDependencies.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga03f5231946f3e850de44120b3fffd58b)
