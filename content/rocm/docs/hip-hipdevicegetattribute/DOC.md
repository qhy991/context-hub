---
name: hip-hipdevicegetattribute
description: "Query for a specific device attribute."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,device-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Device Management
---

# hipDeviceGetAttribute

Query for a specific device attribute.

## Signature

```c
hipError_t hipDeviceGetAttribute(int *pi, hipDeviceAttribute_t attr, int deviceId);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pi` | pointer to value to return |
| [in] | `attr` | attribute to query |
| [in] | `deviceId` | which device to query for information |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga7080a145a4239a7276e0dc22062026c1)
