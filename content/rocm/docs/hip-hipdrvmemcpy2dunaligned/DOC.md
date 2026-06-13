---
name: hip-hipdrvmemcpy2dunaligned
description: "Copies memory for 2D arrays."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Launch API
---

# hipDrvMemcpy2DUnaligned

Copies memory for 2D arrays.

## Signature

```c
hipError_t hipDrvMemcpy2DUnaligned(const hip_Memcpy2D *pCopy);
```

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#gaac4d001873f929f60188c2cd3672de9e)
