---
name: hip-hipmallocarray
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
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMallocArray

Allocate an array on the device.

## Signature

```c
hipError_t hipMallocArray(hipArray_t * array , const hipChannelFormatDesc * desc , size_t width , size_t height , unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `array` | Pointer to allocated array in device memory |
| [in] | `desc` | Requested channel format |
| [in] | `width` | Requested array allocation width |
| [in] | `height` | Requested array allocation height |
| [in] | `flags` | Requested properties of allocated array |

## Returns

hipSuccess , hipErrorOutOfMemory

## See Also

- hipMallocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga8376a0644463118cd96432365bb470e3)
