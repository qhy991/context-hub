---
name: hip-hipruntimegetversion
description: "Returns the approximate HIP Runtime version."
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

# hipRuntimeGetVersion

Returns the approximate HIP Runtime version.

## Signature

```c
hipError_t hipRuntimeGetVersion(int *runtimeVersion);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `runtimeVersion` | HIP runtime version |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#gae8b7ba34d2e11e334650aa51a4dd87ee)
