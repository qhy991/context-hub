---
name: hip-hipdevicegetmempool
description: "Gets the current memory pool for the specified device."
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

# hipDeviceGetMemPool

Gets the current memory pool for the specified device.

## Signature

```c
hipError_t hipDeviceGetMemPool(hipMemPool_t *mem_pool, int device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `mem_pool` | Current memory pool on the specified device |
| [in] | `device` | Device index to query the current memory pool |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotSupported

## Notes

- Returns the last pool provided to hipDeviceSetMemPool for this device or the device's default memory pool if hipDeviceSetMemPool has never been called. By default the current mempool is the default mempool for a device, otherwise the returned pool must have been set with hipDeviceSetMemPool .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga881dfd032ba869936bca97edb1a12ca9)
