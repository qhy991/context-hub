---
name: hip-hiplinkcreate
description: "Creates a linker instance with options."
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

# hipLinkCreate

Creates a linker instance with options.

## Signature

```c
hipError_t hipLinkCreate(unsigned int numOptions, hipJitOption *options, void **optionValues, hipLinkState_t *stateOut);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `numOptions` | Number of options |
| [in] | `options` | Array of options |
| [in] | `optionValues` | Array of option values cast to void* |
| [out] | `stateOut` | hip link state created upon success |

## Returns

hipSuccess hipErrorInvalidValue hipErrorInvalidConfiguration

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga9883986f6bfe2d83f97c7823bae484bd)
