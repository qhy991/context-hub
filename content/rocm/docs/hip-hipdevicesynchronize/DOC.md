---
name: hip-hipdevicesynchronize
description: "Waits on all active streams on current device."
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

# hipDeviceSynchronize

Waits on all active streams on current device.

## Signature

```c
hipError_t hipDeviceSynchronize(void);
```

## Returns

hipSuccess

## Notes

- When this command is invoked, the host thread gets blocked until all the commands associated with streams associated with the device. HIP does not support multiple blocking modes (yet!).

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gaefdc2847fb1d6c3fb1354e827a191ebd)
