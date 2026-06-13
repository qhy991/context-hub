---
name: hip-hiprtclinkadddata
description: "Completes the linking of the given program."
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

# hiprtcLinkAddData

Completes the linking of the given program.

## Signature

```c
hipError_t hiprtcLinkAddData(hiprtcLinkState hip_link_state, hiprtcJITInputType input_type, void *image, size_t image_size, const char *name, unsigned int num_options, hiprtcJIT_option *options_ptr, void **option_values);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hip_link_state` | hiprtc link state |
| [in] | `input_type` | Type of the input data or bitcode |
| [in] | `image` | Input data which is null terminated |
| [in] | `image_size` | Size of the input data |
| [in] | `name` | Optional name for this input |
| [in] | `num_options` | Size of the options |
| [in] | `options_ptr` | Array of options applied to this input |
| [in] | `option_values` | Array of option values cast to void* |

## Returns

HIPRTC_SUCCESS , HIPRTC_ERROR_INVALID_INPUT

## Notes

- If adding the file fails, it will

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga772b8b360f0a1e891ca55fdc32e7e74e)
