---
name: hip-hiplinkcomplete
description: "Completes the linking of the given program."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,module-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Module Management
---

# hipLinkComplete

Completes the linking of the given program.

## Signature

```c
hipError_t hipLinkComplete(hipLinkState_t state, void **hipBinOut, size_t *sizeOut);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `state` | hip link state |
| [out] | `hipBinOut` | Upon success, points to the output binary |
| [out] | `sizeOut` | Size of the binary is stored (optional) |

## Returns

hipSuccess hipErrorInvalidValue

## Notes

- If adding the data fails, it will

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga2bb425497d49cd8245aee333b8024270)
