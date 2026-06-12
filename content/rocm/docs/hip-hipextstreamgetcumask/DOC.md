---
name: hip-hipextstreamgetcumask
description: "Gets CU mask associated with an asynchronous stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Stream Management
---

# hipExtStreamGetCUMask

Gets CU mask associated with an asynchronous stream.

## Signature

```c
hipError_t hipExtStreamGetCUMask(hipStream_t stream, uint32_t cuMaskSize, uint32_t *cuMask);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to be queried |
| [in] | `cuMaskSize` | Number of the block of memories (uint32_t *) allocated by user |
| [out] | `cuMask` | Pointer to a pre-allocated block of memories (uint32_t *) in which the stream's CU mask is returned. The CU mask is returned in a chunck of 32 bits where each active bit represents one active CU. |

## Returns

hipSuccess , hipErrorInvalidHandle , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gaf08dde4ae0b8acdff59bc4f5c77a261b)
