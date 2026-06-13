---
name: hip-hipdevicegettexture1dlinearmaxwidth
description: "Gets the maximum width for 1D linear textures on the specified device."
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

# hipDeviceGetTexture1DLinearMaxWidth

Gets the maximum width for 1D linear textures on the specified device.

## Signature

```c
hipError_t hipDeviceGetTexture1DLinearMaxWidth(size_t *max_width, const hipChannelFormatDesc * desc , int device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `max_width` | Maximum width, in elements, of 1D linear textures that the device can support |
| [in] | `desc` | Requested channel format |
| [in] | `device` | Device index to query for maximum 1D texture width |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDevice

## Notes

- This function queries the maximum width, in elements, of 1D linear textures that can be allocated on the specified device. The maximum width depends on the texture element size and the hardware limitations of the device.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga691821555662759693dfeb9acc7826c7)
