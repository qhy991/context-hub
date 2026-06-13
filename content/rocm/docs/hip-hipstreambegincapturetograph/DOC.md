---
name: hip-hipstreambegincapturetograph
description: "Begins graph capture on a stream to an existing graph."
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

# hipStreamBeginCaptureToGraph

Begins graph capture on a stream to an existing graph.

## Signature

```c
hipError_t hipStreamBeginCaptureToGraph(hipStream_t stream, hipGraph_t graph, const hipGraphNode_t *dependencies, const hipGraphEdgeData *dependencyData, size_t numDependencies, hipStreamCaptureMode mode);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream to initiate capture. |
| [in] | `graph` | - Graph to capture into. |
| [in] | `dependencies` | - Dependencies of the first node captured in the stream. Can be NULL if numDependencies is 0. |
| [in] | `dependencyData` | - Optional array of data associated with each dependency. |
| [in] | `numDependencies` | - Number of dependencies. |
| [in] | `mode` | - Controls the interaction of this capture sequence with other API calls that are not safe. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gabf4070df86154abb92cfc371658d9378)
