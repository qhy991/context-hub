---
name: hip-hiprtclinkaddfile
description: "Adds a file with bit code to be linked with options."
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

# hiprtcLinkAddFile

Adds a file with bit code to be linked with options.

## Signature

```c
hipError_t hiprtcLinkAddFile(hiprtcLinkState hip_link_state, hiprtcJITInputType input_type, const char *file_path, unsigned int num_options, hiprtcJIT_option *options_ptr, void **option_values);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hip_link_state` | hiprtc link state |
| [in] | `input_type` | Type of the input data or bitcode |
| [in] | `file_path` | Path to the input file where bitcode is present |
| [in] | `num_options` | Size of the options |
| [in] | `options_ptr` | Array of options applied to this input |
| [in] | `option_values` | Array of option values cast to void* |

## Returns

HIPRTC_SUCCESS

## Notes

- If input values are invalid, it will

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga1b0f89907c20e8fd1d7e47cbecb80a4b)
