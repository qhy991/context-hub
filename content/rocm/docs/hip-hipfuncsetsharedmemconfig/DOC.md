---
name: hip-hipfuncsetsharedmemconfig
description: "Set shared memory configuation for a specific function."
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

# hipFuncSetSharedMemConfig

Set shared memory configuation for a specific function.

## Signature

```c
hipError_t hipFuncSetSharedMemConfig(const void *func, hipSharedMemConfig config);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `func` | Pointer of the function |
| [in] | `config` | Configuration |

## Returns

hipSuccess , hipErrorInvalidDeviceFunction , hipErrorInvalidValue

## Notes

- Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga36b1d09bfb54678df0c7dc1066ec029c)
