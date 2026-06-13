---
name: hip-hipstreamgetcaptureinfo_v2
description: "Get stream's capture state."
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

# hipStreamGetCaptureInfo_v2

Get stream's capture state.

## Signature

```c
hipError_t hipStreamGetCaptureInfo_v2(hipStream_t stream, hipStreamCaptureStatus *captureStatus_out, unsigned long long *id_out, hipGraph_t *graph_out, const hipGraphNode_t **dependencies_out, size_t *numDependencies_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream of which to get capture status from. |
| [out] | `captureStatus_out` | - Returns current capture status. |
| [out] | `id_out` | - Unique capture ID. |
| [out] | `graph_out` | - Returns the graph being captured into. |
| [out] | `dependencies_out` | - Pointer to an array of nodes representing the graphs dependencies. |
| [out] | `numDependencies_out` | - Returns size of the array returned in dependencies_out. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorStreamCaptureImplicit

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gab794bda84f171bcd1834dd40ed0949b5)
