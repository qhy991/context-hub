---
name: hip-hipmemcpybatchasync
description: "Perform Batch of 1D copies."
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
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpyBatchAsync

Perform Batch of 1D copies.

## Signature

```c
hipError_t hipMemcpyBatchAsync(void **dsts, void **srcs, size_t *sizes, size_t count, hipMemcpyAttributes *attrs, size_t *attrsIdxs, size_t numAttrs, size_t *failIdx, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `dsts` | - Array of destination pointers |
| [in] | `srcs` | - Array of source pointers. |
| [in] | `sizes` | - Array of sizes for memcpy operations |
| [in] | `count` | - Size of dsts, srcs and sizes arrays |
| [in] | `attrs` | - Array of memcpy attributes (not supported) |
| [in] | `attrsIdxs` | - Array of indices to map attrs to copies (not supported) |
| [in] | `numAttrs` | - Size of attrs and attrsIdxs arrays (not supported) |
| [in] | `failIdx` | - Pointer to a location to return failure index inside the batch |
| [in] | `stream` | - stream used to enqueue operations in. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gabd45a88bbd984d686e677d922072f619)
