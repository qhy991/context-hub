---
name: hip-hipmemcpydtoh
description: "Copy data from Device to Host."
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

# hipMemcpyDtoH

Copy data from Device to Host.

## Signature

```c
hipError_t hipMemcpyDtoH(void *dst, hipDeviceptr_t src, size_t sizeBytes);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being copy to |
| [in] | `src` | Data being copy from |
| [in] | `sizeBytes` | Data size in bytes |

## Returns

hipSuccess , hipErrorDeinitialized , hipErrorNotInitialized , hipErrorInvalidContext , hipErrorInvalidValue

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gae61f4e35ff1b9643c6328bc45d091c3f)

## Semantics
Specifically performs a Device-to-Host memory copy. Data is moved from GPU VRAM to CPU system memory over PCIe or xGMI.

## Example
```cpp
#include <hip/hip_runtime.h>

void fetch_results(float* h_dest, const float* d_src, size_t bytes) {
    hipMemcpyDtoH(h_dest, d_src, bytes);
}
```
