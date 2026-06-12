---
name: hip-hipgetprocaddress
description: "Gets the pointer of requested HIP driver function."
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
  hw_unit: driver
  api_module: Memory Management
---

# hipGetProcAddress

Gets the pointer of requested HIP driver function.

## Signature

```c
hipError_t hipGetProcAddress(const char *symbol, void **pfn, int hipVersion, uint64_t flags, hipDriverProcAddressQueryResult *symbolStatus);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `symbol` | The Symbol name of the driver function to request. |
| [out] | `pfn` | Output pointer to the requested driver function. |
| [in] | `hipVersion` | The HIP version for the requested driver function symbol. HIP version is defined as 100*version_major + version_minor. For example, in HIP 6.1, the hipversion is 601, for the symbol function "hipGetDeviceProperties", the specified hipVersion 601 is greater or equal to the version 600, the symbol function will be handle properly as backend compatible function. |
| [in] | `flags` | Currently only default flag is suppported. |
| [out] | `symbolStatus` | Optional enumeration for returned status of searching for symbol driver function based on the input hipVersion. |

## Returns

hipSuccess , hipErrorInvalidValue .

## Notes

- Returns hipSuccess if the returned pfn is addressed to the pointer of found driver function.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga7823a32f9f6f133612c6288a0932bbc2)
