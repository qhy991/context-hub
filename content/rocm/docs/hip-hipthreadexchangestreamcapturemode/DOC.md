---
name: hip-hipthreadexchangestreamcapturemode
description: "Swaps the stream capture mode of a thread."
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

# hipThreadExchangeStreamCaptureMode

Swaps the stream capture mode of a thread.

## Signature

```c
hipError_t hipThreadExchangeStreamCaptureMode(hipStreamCaptureMode *mode);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `mode` | - Pointer to mode value to swap with the current mode. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaa5d692f2f09cad68b7534917e76d8c7f)
