---
name: hip-hipmallocpitch
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

# hipMallocPitch

Allocates at least width (in bytes) * height bytes of linear memory Padding may occur to ensure alighnment requirements are met for the given row The change in width size due to padding will be returned in *pitch. Currently the alignment is set to 128 bytes

## Signature

```c
hipError_t hipMallocPitch(void **ptr, size_t * pitch , size_t width , size_t height);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | Pointer to the allocated device memory |
| [out] | `pitch` | Pitch for allocation (in bytes) |
| [in] | `width` | Requested pitched allocation width (in bytes) |
| [in] | `height` | Requested pitched allocation height |

## Returns

Error code

## Notes

- If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga805c7320498926e444616fe090c727ee)
