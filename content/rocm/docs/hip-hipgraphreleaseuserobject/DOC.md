---
name: hip-hipgraphreleaseuserobject
description: "Release user object from graphs."
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

# hipGraphReleaseUserObject

Release user object from graphs.

## Signature

```c
hipError_t hipGraphReleaseUserObject(hipGraph_t graph, hipUserObject_t object, unsigned int count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `graph` | - pointer to graph to retain the user object for. |
| [in] | `object` | - pointer to instace of userobj. |
| [in] | `count` | - reference to resource to be retained. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga3287f181e8e0999c6774ac37ba04ee8f)
