---
name: hip-hipmemcpy3d
description: "Copies data between host and device."
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

# hipMemcpy3D

Copies data between host and device.

## Signature

```c
hipError_t hipMemcpy3D(const struct hipMemcpy3DParms *p);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `p` | 3D memory copy parameters |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidPitchValue , hipErrorInvalidDevicePointer , hipErrorInvalidMemcpyDirection

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga38facb98eb1ae8206376c3c48bf5c444)

## Semantics
Copies a 3D block of memory. Utilizes `hipMemcpy3DParms` to describe the 3D extent, source/destination pointers, and pitch/slice configurations. Handled by the SDMA engine via specialized 3D linear-to-linear, linear-to-tiled, or tiled-to-tiled transfers.

## Example
```cpp
#include <hip/hip_runtime.h>

void copy_3d(hipPitchedPtr dest, hipPitchedPtr src, hipExtent extent) {
    hipMemcpy3DParms params = {0};
    params.srcPtr = src;
    params.dstPtr = dest;
    params.extent = extent;
    params.kind = hipMemcpyDeviceToDevice;
    hipMemcpy3D(&params);
}
```
