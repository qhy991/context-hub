---
name: hip-hiperror_t
description: "Developer note - when updating these, update the hipErrorName and hipErrorString functions in"
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

# hipError_t

Developer note - when updating these, update the hipErrorName and hipErrorString functions in

## Type

Enum. typedef enum __HIP_NODISCARD hipError_t {

## Values

`hipSuccess`, `hipErrorInvalidValue`, `hipErrorOutOfMemory`, `hipErrorMemoryAllocation`, `hipErrorNotInitialized`, `hipErrorInitializationError`, `hipErrorDeinitialized`, `hipErrorProfilerDisabled`, `hipErrorProfilerNotInitialized`, `hipErrorProfilerAlreadyStarted`, `hipErrorProfilerAlreadyStopped`, `hipErrorInvalidConfiguration`, `hipErrorInvalidPitchValue`, `hipErrorInvalidSymbol`, `hipErrorInvalidDevicePointer`

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga6742b54e2b83c1a5d6861ede4825aafe)
