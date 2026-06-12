---
name: hip-hipfuncsetcacheconfig
description: "Set Cache configuration for a specific function."
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

# hipFuncSetCacheConfig

Set Cache configuration for a specific function.

## Signature

```c
hipError_t hipFuncSetCacheConfig(const void *func, hipFuncCache_t config);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `func` | Pointer of the function. |
| [in] | `config` | Configuration to set. |

## Returns

hipSuccess , hipErrorNotInitialized Note: AMD devices and some Nvidia GPUS do not support reconfigurable cache. This hint is ignored on those architectures.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#gafdb33ef569eb89808fc5178d04b508ba)
