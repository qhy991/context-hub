---
name: hip-hipfuncgetattribute
description: "Find out a specific attribute for a given function."
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

# hipFuncGetAttribute

Find out a specific attribute for a given function.

## Signature

```c
hipError_t hipFuncGetAttribute(int *value, hipFunction_attribute attrib, hipFunction_t hfunc);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `value` | Pointer to the value |
| [in] | `attrib` | Attributes of the given funtion |
| [in] | `hfunc` | Function to get attributes from |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDeviceFunction

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga488a7f867a3e46015659b5665071d2eb)
