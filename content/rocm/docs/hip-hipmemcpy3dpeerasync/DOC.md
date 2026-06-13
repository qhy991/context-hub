---
name: hip-hipmemcpy3dpeerasync
description: "Performs 3D memory copies between devices asynchronously."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpy3DPeerAsync

Performs 3D memory copies between devices asynchronously.

## Signature

```c
hipError_t hipMemcpy3DPeerAsync(hipMemcpy3DPeerParms *p, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `p` | - Parameters for memory copy |
| [in] | `stream` | - Stream to enqueue operation in. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaf51d7f03f7945454ea5d15ac7c7ca402)
