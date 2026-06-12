---
name: hip-hipmemallocpitch
description: "Allocates at least width (in bytes) * height bytes of linear memory Padding may occur to ensure alighnment requirements are met for the given row The change in width size due to padding will be returned in *pitch. Currently the alignment is set to 128 bytes"
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

# hipMemAllocPitch

Allocates at least width (in bytes) * height bytes of linear memory Padding may occur to ensure alighnment requirements are met for the given row The change in width size due to padding will be returned in *pitch. Currently the alignment is set to 128 bytes

## Signature

```c
hipError_t hipMemAllocPitch(hipDeviceptr_t *dptr, size_t * pitch , size_t widthInBytes, size_t height , unsigned int elementSizeBytes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dptr` | Pointer to the allocated device memory |
| [out] | `pitch` | Pitch for allocation (in bytes) |
| [in] | `widthInBytes` | Requested pitched allocation width (in bytes) |
| [in] | `height` | Requested pitched allocation height |
| [in] | `elementSizeBytes` | The size of element bytes, should be 4, 8 or 16 |

## Returns

Error code

## Notes

- If size is 0, no memory is allocated, ptr returns nullptr, and hipSuccess is returned. The intended usage of pitch is as a separate parameter of the allocation, used to compute addresses within the 2D array. Given the row and column of an array element of type T, the address is computed as: T pElement = (T*)((char*)BaseAddress + Row * Pitch) + Column;

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad44d400532df8e67a6db45027cd05405)
