---
name: hip-hipdevicegraphmemtrim
description: "Free unused memory reserved for graphs on a specific device and return it back to the OS."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,graph-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Graph Management
---

# hipDeviceGraphMemTrim

Free unused memory reserved for graphs on a specific device and return it back to the OS.

## Signature

```c
hipError_t hipDeviceGraphMemTrim(int device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `device` | - Device for which memory should be trimmed |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#gaf637d203d43c5df6d44a1c509bd43f4d)
