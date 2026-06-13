---
name: hip-hipstreamgetpriority
description: "Queries the priority of a stream."
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

# hipStreamGetPriority

Queries the priority of a stream.

## Signature

```c
hipError_t hipStreamGetPriority(hipStream_t stream, int *priority);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream to be queried |
| [in,out] | `priority` | Pointer to an unsigned integer in which the stream's priority is returned |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidHandle .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gae5a0d1e66035b157149ec10f5c7952be)
