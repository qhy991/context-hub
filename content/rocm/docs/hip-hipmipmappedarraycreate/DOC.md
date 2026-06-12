---
name: hip-hipmipmappedarraycreate
description: "Create a mipmapped array."
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

# hipMipmappedArrayCreate

Create a mipmapped array.

## Signature

```c
hipError_t hipMipmappedArrayCreate(hipMipmappedArray_t *pHandle, HIP_ARRAY3D_DESCRIPTOR *pMipmappedArrayDesc, unsigned int numMipmapLevels);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pHandle` | pointer to mipmapped array |
| [in] | `pMipmappedArrayDesc` | mipmapped array descriptor |
| [in] | `numMipmapLevels` | mipmap level |

## Returns

hipSuccess , hipErrorNotSupported , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#gaadd49ed1c8e2c4d90adb8211779d971f)
