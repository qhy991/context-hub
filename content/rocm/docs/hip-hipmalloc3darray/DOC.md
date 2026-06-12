---
name: hip-hipmalloc3darray
description: "Allocate an array on the device."
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

# hipMalloc3DArray

Allocate an array on the device.

## Signature

```c
hipError_t hipMalloc3DArray(hipArray_t * array , const struct hipChannelFormatDesc * desc , struct hipExtent extent, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `array` | Pointer to allocated array in device memory |
| [in] | `desc` | Requested channel format |
| [in] | `extent` | Requested array allocation width, height and depth |
| [in] | `flags` | Requested properties of allocated array |

## Returns

hipSuccess , hipErrorOutOfMemory

## See Also

- hipMallocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga3be2acb8c75857958ddd1ab949ed4476)
