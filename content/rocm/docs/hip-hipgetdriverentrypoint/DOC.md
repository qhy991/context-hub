---
name: hip-hipgetdriverentrypoint
description: "Gets function pointer of a requested HIP API."
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

# hipGetDriverEntryPoint

Gets function pointer of a requested HIP API.

## Signature

```c
hipError_t hipGetDriverEntryPoint(const char *symbol, void **funcPtr, unsigned long long flags, hipDriverEntryPointQueryResult *driverStatus);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `symbol` | The API base name |
| [out] | `funcPtr` | Pointer to the requested function |
| [in] | `flags` | Flags for the search |
| [out] | `driverStatus` | Optional returned status of the search |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gaa711b3fea8483aecf71e0a1c13af4684)
