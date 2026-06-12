---
name: hip-hipkernelnameref
description: "Returns kernel name reference by function name."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,callback-activity-apis
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Callback Activity APIs
---

# hipKernelNameRef

Returns kernel name reference by function name.

## Signature

```c
hipError_t hipKernelNameRef(const hipFunction_t f);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `f` | Name of function |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___callback.html#ga9b1a12c449cfd33f5a8c9bbe1c35bf0b)
