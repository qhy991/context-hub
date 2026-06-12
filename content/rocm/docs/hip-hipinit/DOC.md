---
name: hip-hipinit
description: "Explicitly initializes the HIP runtime."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,initialization-and-version
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Initialization and Version
---

# hipInit

Explicitly initializes the HIP runtime.

## Signature

```c
hipError_t hipInit(unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `flags` | Initialization flag, should be zero. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Most HIP APIs implicitly initialize the HIP runtime. This API provides control over the timing of the initialization.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga01baa652dda5815c594d047060496caa)
