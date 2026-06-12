---
name: hip-hiphostgetdevicepointer
description: "Get Device pointer from Host Pointer allocated through hipHostMalloc."
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

# hipHostGetDevicePointer

Get Device pointer from Host Pointer allocated through hipHostMalloc.

## Signature

```c
hipError_t hipHostGetDevicePointer(void ** devPtr , void *hstPtr, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `devPtr` | Device Pointer mapped to passed host pointer |
| [in] | `hstPtr` | Host Pointer allocated through hipHostMalloc |
| [in] | `flags` | Flags to be passed for extension |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorOutOfMemory

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga8fa7a0478020b835a24785cd6bb89725)
