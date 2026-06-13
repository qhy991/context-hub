---
name: hip-hipstreamiscapturing
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

# hipStreamIsCapturing

Get stream's capture state.

## Signature

```c
hipError_t hipStreamIsCapturing(hipStream_t stream, hipStreamCaptureStatus *pCaptureStatus);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream of which to get capture status from. |
| [out] | `pCaptureStatus` | - Returns current capture status. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorStreamCaptureImplicit

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga1e6353035e74630a13ad7effd44e3263)
