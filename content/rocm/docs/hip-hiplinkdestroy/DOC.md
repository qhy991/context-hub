---
name: hip-hiplinkdestroy
description: "Deletes the linker instance."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Module Management
---

# hipLinkDestroy

Deletes the linker instance.

## Signature

```c
hipError_t hipLinkDestroy(hipLinkState_t state);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `state` | link state instance |

## Returns

hipSuccess hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga5aad9536fafac972e38efd1efe2c29b9)
