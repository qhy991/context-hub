---
name: hip-hipextgetlinktypeandhopcount
description: "Returns the link type and hop count between two devices."
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
  hw_unit: driver
  api_module: Device Management
---

# hipExtGetLinkTypeAndHopCount

Returns the link type and hop count between two devices.

## Signature

```c
hipError_t hipExtGetLinkTypeAndHopCount(int device1, int device2, uint32_t *linktype, uint32_t *hopcount);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `device1` | Ordinal for device1 |
| [in] | `device2` | Ordinal for device2 |
| [out] | `linktype` | Returns the link type (See hsa_amd_link_info_type_t) between the two devices |
| [out] | `hopcount` | Returns the hop count between the two devices |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Queries and returns the HSA link type and the hop count between the two specified devices.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga633f8eed24c1d27ed55f950aab99fc88)
