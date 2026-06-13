---
name: hip-hippointergetattributes
description: "Returns attributes for the specified pointer."
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

# hipPointerGetAttributes

Returns attributes for the specified pointer.

## Signature

```c
hipError_t hipPointerGetAttributes(hipPointerAttribute_t *attributes, const void *ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `attributes` | attributes for the specified pointer |
| [in] | `ptr` | pointer to get attributes for |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## Notes

- The output parameter 'attributes' has a member named 'type' that describes what memory the pointer is associated with, such as device memory, host memory, managed memory, and others. Otherwise, the API cannot handle the pointer and returns hipErrorInvalidValue .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga7c3e8663feebb7be9fd3a1e5139bcefc)
