---
name: hip-hipmemcpy3dbatchasync
description: "Perform Batch of 3D copies."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpy3DBatchAsync

Perform Batch of 3D copies.

## Signature

```c
hipError_t hipMemcpy3DBatchAsync(size_t numOps, struct hipMemcpy3DBatchOp *opList, size_t *failIdx, unsigned long long flags, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `numOps` | - Total number of memcpy operations. |
| [in] | `opList` | - Array of size numOps containing the actual memcpy operations. |
| [in] | `failIdx` | - Pointer to a location to return the index of the copy where a failure was encountered. |
| [in] | `flags` | - Flags for future use, must be zero now. |
| [in] | `stream` | - The stream to enqueue the operations in. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga0e387e19da9b076424123fcbd4070fb2)
