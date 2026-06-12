---
name: hip-hipipcopenmemhandle
description: "Opens an interprocess memory handle exported from another process and returns a device pointer usable in the local process."
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

# hipIpcOpenMemHandle

Opens an interprocess memory handle exported from another process and returns a device pointer usable in the local process.

## Signature

```c
hipError_t hipIpcOpenMemHandle(void ** devPtr , hipIpcMemHandle_t handle, unsigned int flags);
```

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidContext , hipErrorInvalidDevicePointer

## Notes

- Maps memory exported from another process with hipIpcGetMemHandle into the current device address space. For contexts on different devices hipIpcOpenMemHandle can attempt to enable peer access between the devices as if the user called hipDeviceEnablePeerAccess. This behavior is controlled by the hipIpcMemLazyEnablePeerAccess flag. hipDeviceCanAccessPeer can determine if a mapping is possible.
- Contexts that may open hipIpcMemHandles are restricted in the following way. hipIpcMemHandles from each device in a given process may only be opened by one context per device per other process.
- Memory returned from hipIpcOpenMemHandle must be freed with hipIpcCloseMemHandle.
- Calling hipFree on an exported memory region before calling hipIpcCloseMemHandle in the importing context will result in undefined behavior.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga2ada334c986e10805d58167e260cb0df)
