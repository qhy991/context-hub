---
name: hip-hipmoduleoccupancymaxactiveblockspermultiprocessor
description: "Returns occupancy for a device function."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,occupancy
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Occupancy
---

# hipModuleOccupancyMaxActiveBlocksPerMultiprocessor

Returns occupancy for a device function.

## Signature

```c
hipError_t hipModuleOccupancyMaxActiveBlocksPerMultiprocessor(int *numBlocks, hipFunction_t f, int blockSize, size_t dynSharedMemPerBlk);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `numBlocks` | Returned occupancy |
| [in] | `f` | Kernel function (hipFunction) for which occupancy is calulated |
| [in] | `blockSize` | Block size the kernel is intended to be launched with |
| [in] | `dynSharedMemPerBlk` | Dynamic shared memory usage (in bytes) intended for each block |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___occupancy.html#ga8f2d8a6b4faae54789811b77f86059ab)
