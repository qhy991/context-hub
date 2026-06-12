---
name: hip-hipstreamgetid
description: "Queries the Id of a stream."
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

# hipStreamGetId

Queries the Id of a stream.

## Signature

```c
hipError_t hipStreamGetId(hipStream_t stream, unsigned long long *streamId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to be queried |
| [in,out] | `flags` | Pointer to an unsigned long long in which the stream's id is returned |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidHandle .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga296cfc9c2ffa8b2a3856ba7a7058d7de)
