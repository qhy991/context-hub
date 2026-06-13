---
name: hip-hipkernelgetname
description: "Returns a Kernel Name."
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

# hipKernelGetName

Returns a Kernel Name.

## Signature

```c
hipError_t hipKernelGetName(const char **name, hipKernel_t kernel);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `name` | Returned Kernel Name |
| [in] | `kernel` | Kernel handle to retrieve name |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga8fba95e5de4ae981e7218d619ee245bf)
