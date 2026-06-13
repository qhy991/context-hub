---
name: hip-hiprtcversion
description: "Sets the parameters as major and minor version."
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

# hiprtcVersion

Sets the parameters as major and minor version.

## Signature

```c
hipError_t hiprtcVersion(int *major, int *minor);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `major` | HIP Runtime Compilation major version. |
| [out] | `minor` | HIP Runtime Compilation minor version. |

## Returns

HIPRTC_ERROR_INVALID_INPUT , HIPRTC_SUCCESS

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#gaef1b2a666014e32bb1ced53729e7f8a6)
