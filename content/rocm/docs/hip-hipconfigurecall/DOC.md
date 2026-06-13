---
name: hip-hipconfigurecall
description: "Configure a kernel launch."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,launch-api
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Launch API
---

# hipConfigureCall

Configure a kernel launch.

## Signature

```c
hipError_t hipConfigureCall(dim3 gridDim, dim3 blockDim, size_t sharedMem, hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `gridDim` | grid dimension specified as multiple of blockDim. |
| [in] | `blockDim` | block dimensions specified in work-items |
| [in] | `sharedMem` | Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. |
| [in] | `stream` | Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue

## Notes

- Please note, HIP does not support kernel launch with total work items defined in dimension with size gridDim x blockDim &gt;= 2^32.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___clang.html#gaef4a44fd1dd0ea4a1be33170e10e0e8b)
