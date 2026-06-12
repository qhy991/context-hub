---
name: hip-hipdevicesetlimit
description: "Sets resource limits of current device."
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

# hipDeviceSetLimit

Sets resource limits of current device.

## Signature

```c
hipError_t hipDeviceSetLimit(enum hipLimit_t limit, size_t value);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `limit` | Enum of hipLimit_t to set |
| [in] | `value` | The size of limit value in bytes |

## Returns

hipSuccess , hipErrorUnsupportedLimit , hipErrorInvalidValue

## Notes

- As the input enum limit, hipLimitStackSize sets the limit value of the stack size on the current GPU device, per thread. The limit size can get via hipDeviceGetLimit. The size is in units of 256 dwords, up to the limit (128K - 16).
- hipLimitMallocHeapSize sets the limit value of the heap used by the malloc()/free() calls. For limit size, use the hipDeviceGetLimit API.
- Any other input as default, the funtion will return hipErrorUnsupportedLimit.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gaaa264755a3c1750a12c60aa7807b7fe8)
