---
name: hip-hiprtcdestroyprogram
description: "Destroys an instance of given hiprtcProgram."
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

# hiprtcDestroyProgram

Destroys an instance of given hiprtcProgram.

## Signature

```c
hipError_t hiprtcDestroyProgram(hiprtcProgram *prog);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `prog` | runtime compilation program instance. |

## Returns

HIPRTC_SUCCESS

## Notes

- If prog is NULL, it will return HIPRTC_ERROR_INVALID_INPUT .

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#gaaf03e08e317ee3e50e3af04aade84787)
