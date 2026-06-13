---
name: hip-hipextmallocwithflags
description: "Allocate memory on the default accelerator."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipExtMallocWithFlags

Allocate memory on the default accelerator.

## Signature

```c
hipError_t hipExtMallocWithFlags(void **ptr, size_t sizeBytes, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | Pointer to the allocated memory |
| [in] | `sizeBytes` | Requested memory size |
| [in] | `flags` | Type of memory allocation |

## Returns

hipSuccess , hipErrorOutOfMemory , hipErrorInvalidValue (bad context, null *ptr)

## Notes

- If requested memory size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.
- The memory allocation flag should be either hipDeviceMallocDefault , hipDeviceMallocFinegrained , hipDeviceMallocUncached , or hipMallocSignalMemory . If the flag is any other value, the API returns hipErrorInvalidValue .

## See Also

- hipMallocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga3529b96082582c65b645085491e91309)
