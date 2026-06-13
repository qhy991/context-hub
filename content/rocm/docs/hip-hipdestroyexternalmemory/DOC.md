---
name: hip-hipdestroyexternalmemory
description: "Destroy an external memory object and release resources."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,external-resource-interoperability
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: External Resource Interoperability
---

# hipDestroyExternalMemory

Destroy an external memory object and release resources.

## Signature

```c
hipError_t hipDestroyExternalMemory(hipExternalMemory_t extMem);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `extMem` | External memory object to be destroyed |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## See Also

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)

## References

- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___external.html)
