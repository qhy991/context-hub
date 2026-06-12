---
name: hip-hipgeterrorname
description: "Return hip error as text string form."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,error-handling
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Error Handling
---

# hipGetErrorName

Return hip error as text string form.

## Signature

```c
hipError_t hipGetErrorName(hipError_t hip_error);
```

## Returns

const char pointer to the NULL-terminated error name

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___error.html#gaa9233b8cdf949e6dd4bd09d664932676)
