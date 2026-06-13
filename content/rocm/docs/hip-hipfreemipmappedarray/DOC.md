---
name: hip-hipfreemipmappedarray
description: "Frees a mipmapped array on the device."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Texture Management
---

# hipFreeMipmappedArray

Frees a mipmapped array on the device.

## Signature

```c
hipError_t hipFreeMipmappedArray(hipMipmappedArray_t mipmappedArray);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `mipmappedArray` | - Pointer to mipmapped array to free |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___texture.html#ga0255fc720bfe4164717b99dbd7c954c4)
