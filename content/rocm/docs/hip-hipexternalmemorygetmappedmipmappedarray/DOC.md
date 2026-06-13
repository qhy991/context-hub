---
name: hip-hipexternalmemorygetmappedmipmappedarray
description: "Map an external memory object to a mipmapped array."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,external-resource-interoperability
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: External Resource Interoperability
---

# hipExternalMemoryGetMappedMipmappedArray

Map an external memory object to a mipmapped array.

## Signature

```c
hipError_t hipExternalMemoryGetMappedMipmappedArray(hipMipmappedArray_t *mipmap, hipExternalMemory_t extMem, const hipExternalMemoryMipmappedArrayDesc *mipmapDesc);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `mipmap` | mipmapped array to return |
| [in] | `extMem` | external memory object handle |
| [in] | `mipmapDesc` | external mipmapped array descriptor |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidResourceHandle

## See Also

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)

## References

- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___external.html)
