---
name: hip-hiprtcgetbitcodesize
description: "Gets the size of compiled bitcode by the runtime compilation program instance."
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

# hiprtcGetBitcodeSize

Gets the size of compiled bitcode by the runtime compilation program instance.

## Signature

```c
hipError_t hiprtcGetBitcodeSize(hiprtcProgram prog, size_t *bitcode_size);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |
| [out] | `bitcode_size` | the size of bitcode. |

## Returns

HIPRTC_SUCCESS

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga775e1e9a7a23c169913eaa8eb874f2d6)
