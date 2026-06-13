---
name: hip-hipdestroyexternalsemaphore
description: "Destroy an external semaphore object and release resources."
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

# hipDestroyExternalSemaphore

Destroy an external semaphore object and release resources.

## Signature

```c
hipError_t hipDestroyExternalSemaphore(hipExternalSemaphore_t extSem);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `extSem` | handle to an external memory object |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## See Also

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)

## References

- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___external.html)
