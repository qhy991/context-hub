---
name: hip-hipdevicegetp2pattribute
description: "Returns a value for attribute of link between two devices."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,initialization-and-version
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Initialization and Version
---

# hipDeviceGetP2PAttribute

Returns a value for attribute of link between two devices.

## Signature

```c
hipError_t hipDeviceGetP2PAttribute(int *value, hipDeviceP2PAttr attr, int srcDevice, int dstDevice);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `value` | Pointer of the value for the attrubute |
| [in] | `attr` | enum of hipDeviceP2PAttr to query |
| [in] | `srcDevice` | The source device of the link |
| [in] | `dstDevice` | The destination device of the link |

## Returns

hipSuccess , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver.html#gaed3b34e394dd0bbdf6a02eafd38b8f15)
