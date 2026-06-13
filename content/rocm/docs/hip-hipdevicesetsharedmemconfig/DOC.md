---
name: hip-hipdevicesetsharedmemconfig
description: "The bank width of shared memory on current device is set."
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

# hipDeviceSetSharedMemConfig

The bank width of shared memory on current device is set.

## Signature

```c
hipError_t hipDeviceSetSharedMemConfig(hipSharedMemConfig config);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `config` | Configuration for the bank width of shared memory |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorNotInitialized

## Notes

- Note: AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga9b1f279084e76691cedfbfadf9c717ee)
