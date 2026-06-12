---
name: hip-hipfuncgetattributes
description: "Find out attributes for a given function."
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
  hw_unit: driver
  api_module: Execution Control
---

# hipFuncGetAttributes

Find out attributes for a given function.

## Signature

```c
hipError_t hipFuncGetAttributes(struct hipFuncAttributes *attr, const void *func);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `attr` | Attributes of funtion |
| [in] | `func` | Pointer to the function handle |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDeviceFunction

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga18a72890686975fdd46c7c8a7bb5a607)
