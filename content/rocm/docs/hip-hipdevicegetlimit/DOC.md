---
name: hip-hipdevicegetlimit
description: "Gets resource limits of current device."
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

# hipDeviceGetLimit

Gets resource limits of current device.

## Signature

```c
hipError_t hipDeviceGetLimit(size_t *pValue, enum hipLimit_t limit);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `pValue` | Returns the size of the limit in bytes |
| [in] | `limit` | The limit to query |

## Returns

hipSuccess , hipErrorUnsupportedLimit , hipErrorInvalidValue

## Notes

- The function queries the size of limit value, as required by the input enum value hipLimit_t, which can be either hipLimitStackSize , or hipLimitMallocHeapSize . Any other input as default, the function will return hipErrorUnsupportedLimit .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga8edc85bb9637d6b1eda0d064d141a255)
