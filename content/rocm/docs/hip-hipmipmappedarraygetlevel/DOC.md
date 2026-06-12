---
name: hip-hipmipmappedarraygetlevel
description: "Get a mipmapped array on a mipmapped level."
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

# hipMipmappedArrayGetLevel

Get a mipmapped array on a mipmapped level.

## Signature

```c
hipError_t hipMipmappedArrayGetLevel(hipArray_t *pLevelArray, hipMipmappedArray_t hMipMappedArray, unsigned int level);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `pLevelArray` | Pointer of array |
| [out] | `hMipMappedArray` | Pointer of mipmapped array on the requested mipmap level |
| [out] | `level` | Mipmap level |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga4c2ebc58183765e20a8216ee5660ff75)
