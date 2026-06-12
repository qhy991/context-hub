---
name: hip-hipgetmipmappedarraylevel
description: "Gets a mipmap level of a HIP mipmapped array."
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
  hw_unit: driver
  api_module: Texture Management
---

# hipGetMipmappedArrayLevel

Gets a mipmap level of a HIP mipmapped array.

## Signature

```c
hipError_t hipGetMipmappedArrayLevel(hipArray_t * levelArray , hipMipmappedArray_const_t mipmappedArray , unsigned int level);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `levelArray` | - Returned mipmap level HIP array |
| [in] | `mipmappedArray` | - HIP mipmapped array |
| [in] | `level` | - Mipmap level |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga1ecc39df7764a7dcd5dad7149ffb2bc5)
