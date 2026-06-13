---
name: hip-hipmoduleoccupancymaxpotentialblocksize
description: "determine the grid and block sizes to achieves maximum occupancy for a kernel"
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

# hipModuleOccupancyMaxPotentialBlockSize

determine the grid and block sizes to achieves maximum occupancy for a kernel

## Signature

```c
hipError_t hipModuleOccupancyMaxPotentialBlockSize(int *gridSize, int *blockSize, hipFunction_t f, size_t dynSharedMemPerBlk, int blockSizeLimit);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `gridSize` | minimum grid size for maximum potential occupancy |
| [out] | `blockSize` | block size for maximum potential occupancy |
| [in] | `f` | kernel function for which occupancy is calulated |
| [in] | `dynSharedMemPerBlk` | dynamic shared memory usage (in bytes) intended for each block |
| [in] | `blockSizeLimit` | the maximum block size for the kernel, use 0 for no limit |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Please note, HIP does not support kernel launch with total work items defined in dimension with size gridDim x blockDim &gt;= 2^32.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___occupancy.html#ga322e4690ca20dbf8a07293f2a1105c94)
