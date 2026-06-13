---
name: hip-hipfuncsetattribute
description: "Set attribute for a specific function."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,execution-control
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Execution Control
---

# hipFuncSetAttribute

Set attribute for a specific function.

## Signature

```c
hipError_t hipFuncSetAttribute(const void *func, hipFuncAttribute attr, int value);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `func` | Pointer of the function |
| [in] | `attr` | Attribute to set |
| [in] | `value` | Value to set |

## Returns

hipSuccess , hipErrorInvalidDeviceFunction , hipErrorInvalidValue

## Notes

- Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga8417deea9092f35e497bc7e19bd5e12d)
