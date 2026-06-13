---
name: hip-hiprtcaddnameexpression
description: "Adds the given name exprssion to the runtime compilation program."
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

# hiprtcAddNameExpression

Adds the given name exprssion to the runtime compilation program.

## Signature

```c
hipError_t hiprtcAddNameExpression(hiprtcProgram prog, const char *name_expression);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |
| [in] | `name_expression` | const char pointer to the name expression. |

## Returns

HIPRTC_SUCCESS

## Notes

- If const char pointer is NULL, it will return HIPRTC_ERROR_INVALID_INPUT .

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga050d3a66e5a6fc90284857af3760b142)
