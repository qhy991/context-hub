---
name: hip-hipmemgetinfo
description: "Query memory info."
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

# hipMemGetInfo

Query memory info.

## Signature

```c
hipError_t hipMemGetInfo(size_t *free, size_t *total);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `free` | Returns free memory on the current device in bytes |
| [out] | `total` | Returns total allocatable memory on the current device in bytes |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## Notes

- On ROCM, this function gets the actual free memory left on the current device, so supports the cases while running multi-workload (such as multiple processes, multiple threads, and multiple GPUs).

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga311c3e246a21590de14478b8bd063be2)
