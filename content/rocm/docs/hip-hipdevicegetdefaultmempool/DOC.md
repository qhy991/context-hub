---
name: hip-hipdevicegetdefaultmempool
description: "Returns the default memory pool of the specified device."
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

# hipDeviceGetDefaultMemPool

Returns the default memory pool of the specified device.

## Signature

```c
hipError_t hipDeviceGetDefaultMemPool(hipMemPool_t *mem_pool, int device);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `mem_pool` | Default memory pool to return |
| [in] | `device` | Device index for query the default memory pool |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidValue , hipErrorNotSupported

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga16d31ff3398a0c76ea5148563406412a)
