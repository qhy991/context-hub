---
name: hip-hipgetfuncbysymbol
description: "Gets pointer to device entry function that matches entry function symbolPtr."
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

# hipGetFuncBySymbol

Gets pointer to device entry function that matches entry function symbolPtr.

## Signature

```c
hipError_t hipGetFuncBySymbol(hipFunction_t *functionPtr, const void *symbolPtr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `functionPtr` | Device entry function |
| [in] | `symbolPtr` | Pointer to device entry function to search for |

## Returns

hipSuccess , hipErrorInvalidDeviceFunction

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga4adaac7b90f84ec13b0274df72245547)
