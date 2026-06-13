---
name: hip-hipstreamgetcaptureinfo
description: "Get capture status of a stream."
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

# hipStreamGetCaptureInfo

Get capture status of a stream.

## Signature

```c
hipError_t hipStreamGetCaptureInfo(hipStream_t stream, hipStreamCaptureStatus *pCaptureStatus, unsigned long long *pId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream of which to get capture status from. |
| [out] | `pCaptureStatus` | - Returns current capture status. |
| [out] | `pId` | - Unique capture ID. |

## Returns

hipSuccess , hipErrorStreamCaptureImplicit

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga5343379e3f86d39aa8527fe0e68abf14)
