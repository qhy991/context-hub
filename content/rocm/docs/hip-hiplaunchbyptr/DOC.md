---
name: hip-hiplaunchbyptr
description: "Launch a kernel."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,launch-api
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Launch API
---

# hipLaunchByPtr

Launch a kernel.

## Signature

```c
hipError_t hipLaunchByPtr(const void *func);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `func` | Kernel to launch. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#ga80f5f26fe76b213fbfd77e4fc9e04cbd)
