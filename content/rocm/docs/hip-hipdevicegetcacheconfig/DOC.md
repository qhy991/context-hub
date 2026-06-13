---
name: hip-hipdevicegetcacheconfig
description: "Get Cache configuration for a specific Device."
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

# hipDeviceGetCacheConfig

Get Cache configuration for a specific Device.

## Signature

```c
hipError_t hipDeviceGetCacheConfig(hipFuncCache_t *cacheConfig);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `cacheConfig` | Pointer of cache configuration |

## Returns

hipSuccess , hipErrorNotInitialized Note: AMD devices do not support reconfigurable cache. This hint is ignored on these architectures.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga37057f9830ad6fab7ce5f05f6d3c89ab)
