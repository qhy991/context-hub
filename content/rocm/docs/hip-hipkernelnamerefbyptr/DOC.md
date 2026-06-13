---
name: hip-hipkernelnamerefbyptr
description: "Retrives kernel for a given host pointer, unless stated otherwise."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,callback-activity-apis
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Callback Activity APIs
---

# hipKernelNameRefByPtr

Retrives kernel for a given host pointer, unless stated otherwise.

## Signature

```c
hipError_t hipKernelNameRefByPtr(const void *hostFunction, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hostFunction` | Pointer of host function. |
| [in] | `stream` | Stream the kernel is executed on. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___callback.html#gaa08d00225c8cca17417fe2b9abce1088)
