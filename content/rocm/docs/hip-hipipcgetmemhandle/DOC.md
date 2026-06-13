---
name: hip-hipipcgetmemhandle
description: "Gets an interprocess memory handle for an existing device memory allocation."
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

# hipIpcGetMemHandle

Gets an interprocess memory handle for an existing device memory allocation.

## Signature

```c
hipError_t hipIpcGetMemHandle(hipIpcMemHandle_t *handle, void * devPtr);
```

## Returns

hipSuccess , hipErrorInvalidHandle , hipErrorOutOfMemory , hipErrorMapFailed

## Notes

- Takes a pointer to the base of an existing device memory allocation created with hipMalloc and exports it for use in another process. This is a lightweight operation and may be called multiple times on an allocation without adverse effects.
- If a region of memory is freed with hipFree and a subsequent call to hipMalloc returns memory with the same device address, hipIpcGetMemHandle will return a unique handle for the new memory.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gafd8c80f7e3b6426a630fff768409be70)
