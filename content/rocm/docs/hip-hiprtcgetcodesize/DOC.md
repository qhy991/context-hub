---
name: hip-hiprtcgetcodesize
description: "Gets the size of compilation binary by the runtime compilation program instance."
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

# hiprtcGetCodeSize

Gets the size of compilation binary by the runtime compilation program instance.

## Signature

```c
hipError_t hiprtcGetCodeSize(hiprtcProgram prog, size_t *codeSizeRet);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |
| [out] | `codeSizeRet` | the size of binary. |

## Returns

HIPRTC_SUCCESS

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga3dce3c4183d7a09c9ffffd763f744ecb)
