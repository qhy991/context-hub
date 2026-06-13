---
name: hip-hipdevicesetmempool
description: "Sets the current memory pool of a device."
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

# hipDeviceSetMemPool

Sets the current memory pool of a device.

## Signature

```c
hipError_t hipDeviceSetMemPool(int device, hipMemPool_t mem_pool);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `device` | Device index for the update |
| [in] | `mem_pool` | Memory pool for update as the current on the specified device |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDevice , hipErrorNotSupported

## Notes

- The memory pool must be local to the specified device. hipMallocAsync allocates from the current mempool of the provided stream's device. By default, a device's current memory pool is its default memory pool.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga29fd231db3cb31fde8f776d5b073e407)
