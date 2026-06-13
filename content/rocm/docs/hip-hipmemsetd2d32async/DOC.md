---
name: hip-hipmemsetd2d32async
description: "Fills 2D memory range of 'width' 32-bit values asynchronously to the specified int value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row."
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

# hipMemsetD2D32Async

Fills 2D memory range of 'width' 32-bit values asynchronously to the specified int value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row.

## Signature

```c
hipError_t hipMemsetD2D32Async(hipDeviceptr_t dst, size_t dstPitch, unsigned int value, size_t width , size_t height , hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dst` | Pointer to device memory |
| [in] | `dstPitch` | Pitch of dst device pointer |
| [in] | `value` | value to set |
| [in] | `width` | Width of row |
| [in] | `height` | Number of rows |
| [in] | `stream` | Stream Identifier |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga675985ebfe6611556955dc88195937d6)
