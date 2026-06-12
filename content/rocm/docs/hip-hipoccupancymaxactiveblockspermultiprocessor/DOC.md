---
name: hip-hipoccupancymaxactiveblockspermultiprocessor
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
  hw_unit: driver
  api_module: Occupancy
---

# hipOccupancyMaxActiveBlocksPerMultiprocessor

Returns occupancy for a device function.

## Signature

```c
hipError_t hipOccupancyMaxActiveBlocksPerMultiprocessor(int *numBlocks, const void *f, int blockSize, size_t dynSharedMemPerBlk);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `numBlocks` | Returned occupancy |
| [in] | `f` | Kernel function for which occupancy is calulated |
| [in] | `blockSize` | Block size the kernel is intended to be launched with |
| [in] | `dynSharedMemPerBlk` | Dynamic shared memory usage (in bytes) intended for each block |

## Returns

hipSuccess , hipErrorInvalidDeviceFunction , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___occupancy.html#ga59c488f35b0ba4b4938ba16e1a7ed7ec)
