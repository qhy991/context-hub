---
name: hip-hipstreambatchmemop
description: "Enqueues an array of stream memory operations in the stream.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-memory-operations
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Stream Memory Operations
---

# hipStreamBatchMemOp

Enqueues an array of stream memory operations in the stream.[BETA].

## Signature

```c
hipError_t hipStreamBatchMemOp(hipStream_t stream, unsigned int count, hipStreamBatchMemOpParams *paramArray, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream identifier |
| [in] | `count` | - The number of operations in the array. Must be less than 256 |
| [in] | `paramArray` | - The types and parameters of the individual operations. |
| [in] | `flags` | - Reserved for future expansion; must be 0. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Batch operations to synchronize the stream via memory operations.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#gab85e2279338d18c4cf6f4cf4c895ad95)
