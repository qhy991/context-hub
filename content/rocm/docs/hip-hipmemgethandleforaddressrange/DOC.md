---
name: hip-hipmemgethandleforaddressrange
description: "Returns a handle for the address range requested."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,module-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Module Management
---

# hipMemGetHandleForAddressRange

Returns a handle for the address range requested.

## Signature

```c
hipError_t hipMemGetHandleForAddressRange(void *handle, hipDeviceptr_t dptr, size_t size , hipMemRangeHandleType handleType, unsigned long long flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `handle` | Ptr to the handle where the fd or other types will be returned. |
| [in] | `dptr` | Device ptr for which we get the handle. |
| [in] | `size` | Size of the address range. |
| [in] | `handleType` | Type of the handle requested for the address range. |
| [in] | `flags` | Any flags set regarding the handle requested. |

## Returns

hipSuccess if the kernel is launched successfully, otherwise an appropriate error code.

## Notes

- This function returns a handle to a device pointer created using either hipMalloc set of APIs or through hipMemAddressReserve (as long as the ptr is mapped).

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#ga641bf30f80c5483db4c13eda7b37cb5d)
