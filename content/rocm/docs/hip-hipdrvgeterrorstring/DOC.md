---
name: hip-hipdrvgeterrorstring
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

# hipDrvGetErrorString

Return handy text string message to explain the error which occurred.

## Signature

```c
hipError_t hipDrvGetErrorString(hipError_t hipError, const char **errorString);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hipError` | Error code to convert to string. |
| [out] | `errorString` | char pointer to the NULL-terminated error string |

## Returns

hipSuccess , hipErrorInvalidValue

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___error.html#ga3aa89ef36e29e1f03b8d3450d05dcf96)
