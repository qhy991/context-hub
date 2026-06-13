---
name: hip-hipsetupargument
description: "Set a kernel argument."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,launch-api
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Launch API
---

# hipSetupArgument

Set a kernel argument.

## Signature

```c
hipError_t hipSetupArgument(const void *arg, size_t size , size_t offset);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `arg` | Pointer the argument in host memory. |
| [in] | `size` | Size of the argument. |
| [in] | `offset` | Offset of the argument on the argument stack. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#ga047cff6205399540ebe31cdd11257c07)
