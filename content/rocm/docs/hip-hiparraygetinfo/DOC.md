---
name: hip-hiparraygetinfo
description: "Gets info about the specified array."
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

# hipArrayGetInfo

Gets info about the specified array.

## Signature

```c
hipError_t hipArrayGetInfo(hipChannelFormatDesc * desc , hipExtent *extent, unsigned int *flags, hipArray_t array);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `desc` | - Returned array type |
| [out] | `extent` | - Returned array shape. 2D arrays will have depth of zero |
| [out] | `flags` | - Returned array flags |
| [in] | `array` | - The HIP array to get info for |

## Returns

hipSuccess , hipErrorInvalidValue hipErrorInvalidHandle

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga9f67e594f3d410393b312ade84044597)
