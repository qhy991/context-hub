---
name: hip-hipgeterrorstring
description: "Return handy text string message to explain the error which occurred."
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

# hipGetErrorString

Return handy text string message to explain the error which occurred.

## Signature

```c
hipError_t hipGetErrorString(hipError_t hipError);
```

## Returns

const char pointer to the NULL-terminated error string

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___error.html#ga045c60abfb65927aabc7e6e1e3d2598b)
