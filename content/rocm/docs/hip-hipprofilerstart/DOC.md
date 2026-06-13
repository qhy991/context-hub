---
name: hip-hipprofilerstart
description: "Start recording of profiling information [Deprecated] When using this API, start the profiler with profiling disabled. (&ndash;startdisabled)"
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,profiler-control
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Profiler Control
---

# hipProfilerStart

Start recording of profiling information [Deprecated] When using this API, start the profiler with profiling disabled. (&ndash;startdisabled)

## Signature

```c
hipError_t hipProfilerStart();
```

## Returns

hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___profiler.html#ga40aa20d731f9c8f0586127d589759e1d)
