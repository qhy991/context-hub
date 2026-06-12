---
name: hip-hipdevicegetgraphmemattribute
description: "Get the mem attribute for graphs."
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

# hipDeviceGetGraphMemAttribute

Get the mem attribute for graphs.

## Signature

```c
hipError_t hipDeviceGetGraphMemAttribute(int device, hipGraphMemAttributeType attr, void *value);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `device` | - Device to get attributes from |
| [in] | `attr` | - Attribute type to be queried |
| [out] | `value` | - Value of the queried attribute |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga5eb353becf0e5a38a376dd7aa13677c0)
