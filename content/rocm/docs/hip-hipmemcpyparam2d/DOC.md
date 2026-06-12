---
name: hip-hipmemcpyparam2d
description: "Copies memory for 2D arrays."
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
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpyParam2D

Copies memory for 2D arrays.

## Signature

```c
hipError_t hipMemcpyParam2D(const hip_Memcpy2D *pCopy);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `pCopy` | Parameters for the memory copy |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaa6913c5738f524d8fd043ab6f2c0e5ed)
