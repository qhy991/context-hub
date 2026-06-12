---
name: hip-hiprtcgeterrorstring
description: "Returns text string message to explain the error which occurred."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,runtime-compilation
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Runtime Compilation
---

# hiprtcGetErrorString

Returns text string message to explain the error which occurred.

## Signature

```c
hipError_t hiprtcGetErrorString(hiprtcResult result);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `result` | code to convert to string. |

## Returns

const char pointer to the NULL-terminated error string

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga27bebf4ed3e810ca627cbbfc34880be1)
