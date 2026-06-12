---
name: hip-hiprtclinkcreate
description: "Creates the link instance via hiprtc APIs."
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

# hiprtcLinkCreate

Creates the link instance via hiprtc APIs.

## Signature

```c
hipError_t hiprtcLinkCreate(unsigned int num_options, hiprtcJIT_option *option_ptr, void **option_vals_pptr, hiprtcLinkState *hip_link_state_ptr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `num_options` | Number of options |
| [in] | `option_ptr` | Array of options |
| [in] | `option_vals_pptr` | Array of option values cast to void* |
| [out] | `hip_link_state_ptr` | hiprtc link state created upon success |

## Returns

HIPRTC_SUCCESS , HIPRTC_ERROR_INVALID_INPUT , HIPRTC_ERROR_INVALID_OPTION

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga39f7dee1fb248b9b3977b53c18deea8d)
