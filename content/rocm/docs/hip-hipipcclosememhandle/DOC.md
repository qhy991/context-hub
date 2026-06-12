---
name: hip-hipipcclosememhandle
description: "Close memory mapped with hipIpcOpenMemHandle."
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

# hipIpcCloseMemHandle

Close memory mapped with hipIpcOpenMemHandle.

## Signature

```c
hipError_t hipIpcCloseMemHandle(void * devPtr);
```

## Returns

hipSuccess , hipErrorMapFailed , hipErrorInvalidHandle

## Notes

- Unmaps memory returnd by hipIpcOpenMemHandle. The original allocation in the exporting process as well as imported mappings in other processes will be unaffected.
- Any resources used to enable peer access will be freed if this is the last mapping using them.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gac2db0688a6a471e17ca631977e199da7)
