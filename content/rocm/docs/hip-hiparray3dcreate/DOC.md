---
name: hip-hiparray3dcreate
description: "Create a 3D array memory pointer on the device."
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

# hipArray3DCreate

Create a 3D array memory pointer on the device.

## Signature

```c
hipError_t hipArray3DCreate(hipArray_t * array , const HIP_ARRAY3D_DESCRIPTOR *pAllocateArray);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `array` | Pointer to the 3D array memory |
| [in] | `pAllocateArray` | Requested array desciptor |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga9dc08dfcd1078227106d9a4a3fe77d25)
