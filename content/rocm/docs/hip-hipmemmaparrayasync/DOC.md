---
name: hip-hipmemmaparrayasync
description: "Maps or unmaps subregions of sparse HIP arrays and sparse HIP mipmapped arrays."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,virtual-memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Virtual Memory Management
---

# hipMemMapArrayAsync

Maps or unmaps subregions of sparse HIP arrays and sparse HIP mipmapped arrays.

## Signature

```c
hipError_t hipMemMapArrayAsync(hipArrayMapInfo *mapInfoList, unsigned int count, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `mapInfoList` | - list of hipArrayMapInfo . |
| [in] | `count` | - number of hipArrayMapInfo in mapInfoList. |
| [in] | `stream` | - stream identifier for the stream to use for map or unmap operations. |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___virtual.html#gaceac55fcd2ca672259ef929d4e0461c4)
