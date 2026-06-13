---
name: hip-hiparray3dgetdescriptor
description: "Gets a 3D array descriptor."
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

# hipArray3DGetDescriptor

Gets a 3D array descriptor.

## Signature

```c
hipError_t hipArray3DGetDescriptor(HIP_ARRAY3D_DESCRIPTOR *pArrayDescriptor, hipArray_t array);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pArrayDescriptor` | - Returned 3D array descriptor |
| [in] | `array` | - 3D array to get descriptor of |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue hipErrorInvalidHandle , hipErrorContextIsDestroyed

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga68d59254ab8994d3f61063bb57bf5498)
