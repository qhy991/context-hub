---
name: hip-hipoccupancyavailabledynamicsmemperblock
description: "Returns dynamic shared memory available per block when launching numBlocks blocks on SM."
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

# hipOccupancyAvailableDynamicSMemPerBlock

Returns dynamic shared memory available per block when launching numBlocks blocks on SM.

## Signature

```c
hipError_t hipOccupancyAvailableDynamicSMemPerBlock(size_t *dynamicSmemSize, const void *f, int numBlocks, int blockSize);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dynamicSmemSize` | Returned maximum dynamic shared memory. |
| [in] | `f` | Kernel function for which occupancy is calculated. |
| [in] | `numBlocks` | Number of blocks to fit on SM |
| [in] | `blockSize` | Size of the block |

## Returns

hipSuccess , hipErrorInvalidDevice , hipErrorInvalidDeviceFunction , hipErrorInvalidValue , hipErrorUnknown

## Notes

- Returns in *dynamicSmemSize the maximum size of dynamic shared memory / to allow numBlocks blocks per SM.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___occupancy.html#ga1803172546906e8e48c5b3141263afa1)
