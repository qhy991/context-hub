---
name: hip-hipdrvmemcpy3d
description: "Copies data between host and device."
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

# hipDrvMemcpy3D

Copies data between host and device.

## Signature

```c
hipError_t hipDrvMemcpy3D(const HIP_MEMCPY3D *pCopy);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `pCopy` | 3D memory copy parameters |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaa385d7b1d0f0d941224abd9549ea9494)
