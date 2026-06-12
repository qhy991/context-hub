---
name: hip-hipdevicesetgraphmemattribute
description: "Set the mem attribute for graphs."
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
  hw_unit: driver
  api_module: Graph Management
---

# hipDeviceSetGraphMemAttribute

Set the mem attribute for graphs.

## Signature

```c
hipError_t hipDeviceSetGraphMemAttribute(int device, hipGraphMemAttributeType attr, void *value);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `device` | - Device to set attribute of. |
| [in] | `attr` | - Attribute type to be set. |
| [in] | `value` | - Value of the attribute. |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga0921c547b41f9124bb4aec6d5f7dab46)
