---
name: hip-hiprtclinkcomplete
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

# hiprtcLinkComplete

Completes the linking of the given program.

## Signature

```c
hipError_t hiprtcLinkComplete(hiprtcLinkState hip_link_state, void **bin_out, size_t *size_out);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hip_link_state` | hiprtc link state |
| [out] | `bin_out` | Upon success, points to the output binary |
| [out] | `size_out` | Size of the binary is stored (optional) |

## Returns

HIPRTC_SUCCESS

## Notes

- If adding the data fails, it will

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga1479cebdfe7986b909531d2ee37714b2)
