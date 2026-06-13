---
name: hip-hipfreearray
description: "Frees an array on the device."
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

# hipFreeArray

Frees an array on the device.

## Signature

```c
hipError_t hipFreeArray(hipArray_t array);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `array` | Pointer to array to free |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized

## See Also

- hipMallocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gad6c25b3106fb47a2a75285ff2bd8cb29)
