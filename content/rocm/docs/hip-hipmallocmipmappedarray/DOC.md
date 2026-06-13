---
name: hip-hipmallocmipmappedarray
description: "Allocate a mipmapped array on the device."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,texture-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Texture Management
---

# hipMallocMipmappedArray

Allocate a mipmapped array on the device.

## Signature

```c
hipError_t hipMallocMipmappedArray(hipMipmappedArray_t * mipmappedArray , const struct hipChannelFormatDesc * desc , struct hipExtent extent, unsigned int numLevels, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `mipmappedArray` | - Pointer to allocated mipmapped array in device memory |
| [in] | `desc` | - Requested channel format |
| [in] | `extent` | - Requested allocation size (width field in elements) |
| [in] | `numLevels` | - Number of mipmap levels to allocate |
| [in] | `flags` | - Flags for extensions |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorMemoryAllocation

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gace6d42a4c294a5fe5cb9a383aca7eb36)
