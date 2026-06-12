---
name: hip-hiprtccreateprogram
description: "Creates an instance of hiprtcProgram with the given input parameters, and sets the output hiprtcProgram prog with it."
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

# hiprtcCreateProgram

Creates an instance of hiprtcProgram with the given input parameters, and sets the output hiprtcProgram prog with it.

## Signature

```c
hipError_t hiprtcCreateProgram(hiprtcProgram *prog, const char *src, const char *name, int numHeaders, const char *const *headers, const char *const *includeNames);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `prog` | runtime compilation program instance. |
| [in] | `src` | const char pointer to the program source. |
| [in] | `name` | const char pointer to the program name. |
| [in] | `numHeaders` | number of headers. |
| [in] | `headers` | array of strings pointing to headers. |
| [in] | `includeNames` | array of strings pointing to names included in program source. |

## Returns

HIPRTC_SUCCESS

## Notes

- Any invalide input parameter, it will return HIPRTC_ERROR_INVALID_INPUT or HIPRTC_ERROR_INVALID_PROGRAM .
- If failed to create the program, it will return HIPRTC_ERROR_PROGRAM_CREATION_FAILURE .

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#gae7ab5939a3f85ef3b7dcad3314f3067c)
