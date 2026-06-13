---
name: hip-hipmemcpywithstream
description: "Memory copy on the stream. It allows single or multiple devices to do memory copy on single or multiple streams."
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

# hipMemcpyWithStream

Memory copy on the stream. It allows single or multiple devices to do memory copy on single or multiple streams.

## Signature

```c
hipError_t hipMemcpyWithStream(void *dst, const void *src, size_t sizeBytes, hipMemcpyKind kind, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being copy to |
| [in] | `src` | Data being copy from |
| [in] | `sizeBytes` | Data size in bytes |
| [in] | `kind` | Kind of transfer |
| [in] | `stream` | Valid stream |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorUnknown , hipErrorContextIsDestroyed

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gae9ba7e2beacec0bd9d606ec8d241da37)
