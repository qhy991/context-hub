---
name: hip-hipdrivergetversion
description: "Returns the approximate HIP driver version."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Initialization and Version
---

# hipDriverGetVersion

Returns the approximate HIP driver version.

## Signature

```c
hipError_t hipDriverGetVersion(int *driverVersion);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `driverVersion` | driver version |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- HIP driver version shows up in the format: HIP_VERSION_MAJOR * 10000000 + HIP_VERSION_MINOR * 100000 + HIP_VERSION_PATCH.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#gaf6c342f52d2a29a0aca5cdd89b4dd47c)
