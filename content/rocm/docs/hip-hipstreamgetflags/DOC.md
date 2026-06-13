---
name: hip-hipstreamgetflags
description: "Returns flags associated with this stream."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Management
---

# hipStreamGetFlags

Returns flags associated with this stream.

## Signature

```c
hipError_t hipStreamGetFlags(hipStream_t stream, unsigned int *flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to be queried |
| [in,out] | `flags` | Pointer to an unsigned integer in which the stream's flags are returned |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidHandle .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#ga3249555a26439591b8873f70b39bb116)
