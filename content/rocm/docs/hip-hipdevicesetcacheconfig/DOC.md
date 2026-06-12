---
name: hip-hipdevicesetcacheconfig
description: "Set L1/Shared cache partition."
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

# hipDeviceSetCacheConfig

Set L1/Shared cache partition.

## Signature

```c
hipError_t hipDeviceSetCacheConfig(hipFuncCache_t cacheConfig);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `cacheConfig` | Cache configuration |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorNotSupported

## Notes

- Note: AMD devices do not support reconfigurable cache. This API is not implemented on AMD platform. If the function is called, it will return hipErrorNotSupported.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gaada3d30a46ae06f68cf1574f496b86ee)
