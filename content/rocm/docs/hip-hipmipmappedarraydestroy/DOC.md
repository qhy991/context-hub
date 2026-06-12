---
name: hip-hipmipmappedarraydestroy
description: "Destroy a mipmapped array."
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

# hipMipmappedArrayDestroy

Destroy a mipmapped array.

## Signature

```c
hipError_t hipMipmappedArrayDestroy(hipMipmappedArray_t hMipmappedArray);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `hMipmappedArray` | pointer to mipmapped array to destroy |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga4e5dd69cb90ff4d93aab4d6bff2cbcda)
