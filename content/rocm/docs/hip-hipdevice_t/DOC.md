---
name: hip-hipdevice_t
description: "Note many APIs also use integer deviceIds as an alternative to the device pointer:"
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

# hipDevice_t

Note many APIs also use integer deviceIds as an alternative to the device pointer:

## Type

Type alias. typedef int hipDevice_t;

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#ga181a06ca0d50ffdd6e019c87ffe02fb4)
