---
name: hip-hiparraygetdescriptor
description: "Gets a 1D or 2D array descriptor."
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

# hipArrayGetDescriptor

Gets a 1D or 2D array descriptor.

## Signature

```c
hipError_t hipArrayGetDescriptor(HIP_ARRAY_DESCRIPTOR *pArrayDescriptor, hipArray_t array);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pArrayDescriptor` | - Returned array descriptor |
| [in] | `array` | - Array to get descriptor of |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue hipErrorInvalidHandle

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga6e64255c46778f5839711fe730cc7abc)
