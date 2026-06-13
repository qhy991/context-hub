---
name: hip-hipwaitexternalsemaphoresasync
description: "Waits on a set of external semaphore objects."
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

# hipWaitExternalSemaphoresAsync

Waits on a set of external semaphore objects.

## Signature

```c
hipError_t hipWaitExternalSemaphoresAsync(const hipExternalSemaphore_t *extSemArray, const hipExternalSemaphoreWaitParams *paramsArray, unsigned int numExtSems, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `extSemArray` | External semaphores to be waited on |
| [in] | `paramsArray` | Array of semaphore parameters |
| [in] | `numExtSems` | Number of semaphores to wait on |
| [in] | `stream` | Stream to enqueue the wait operations in |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## See Also

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)

## References

- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___external.html)
