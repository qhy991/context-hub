---
name: hip-hiprtccompileprogram
description: "Compiles the given runtime compilation program."
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

# hiprtcCompileProgram

Compiles the given runtime compilation program.

## Signature

```c
hipError_t hiprtcCompileProgram(hiprtcProgram prog, int numOptions, const char *const *options);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |
| [in] | `numOptions` | number of compiler options. |
| [in] | `options` | compiler options as const array of strins. |

## Returns

HIPRTC_SUCCESS

## Notes

- If the compiler failed to build the runtime compilation program, it will return HIPRTC_ERROR_COMPILATION .

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga7f44ccee23232dbc3e73dbedd4d3f2ad)
