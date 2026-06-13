---
name: hip-hiprtcgetloweredname
description: "Gets the lowered (mangled) name from an instance of hiprtcProgram with the given input parameters, and sets the output lowered_name with it."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Runtime Compilation
---

# hiprtcGetLoweredName

Gets the lowered (mangled) name from an instance of hiprtcProgram with the given input parameters, and sets the output lowered_name with it.

## Signature

```c
hipError_t hiprtcGetLoweredName(hiprtcProgram prog, const char *name_expression, const char **lowered_name);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |
| [in] | `name_expression` | const char pointer to the name expression. |
| [in,out] | `lowered_name` | const char array to the lowered (mangled) name. |

## Returns

HIPRTC_SUCCESS

## Notes

- If any invalide nullptr input parameters, it will return HIPRTC_ERROR_INVALID_INPUT
- If name_expression is not found, it will return HIPRTC_ERROR_NAME_EXPRESSION_NOT_VALID
- If failed to get lowered_name from the program, it will return HIPRTC_ERROR_COMPILATION .

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga1e890947c8786af8f3a3eeda2280a5cc)
