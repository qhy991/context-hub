---
name: hip-hipmemcpy
description: "Copy data from src to dst."
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

# hipMemcpy

Copy data from src to dst.

## Signature

```c
hipError_t hipMemcpy(void *dst, const void *src, size_t sizeBytes, hipMemcpyKind kind);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `dst` | Data being copy to |
| [in] | `src` | Data being copy from |
| [in] | `sizeBytes` | Data size in bytes |
| [in] | `kind` | Kind of transfer |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorUnknown

## Notes

- It supports memory from host to device, device to host, device to device and host to host The src and dst must not overlap.
- For hipMemcpy, the copy is always performed by the current device (set by hipSetDevice). For multi-gpu or peer-to-peer configurations, it is recommended to set the current device to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess with copy agent as the current device and src/dst as the peerDevice argument. if this is not done, the hipMemcpy will still work, but will perform the copy using a staging buffer on the host. Calling hipMemcpy with dst and src pointers that do not match the hipMemcpyKind results in undefined behavior.

## See Also

- hipMemAllocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gac1a055d288302edd641c6d7416858e1e)

## Semantics
Copies data between host and device or device and device. It automatically infers the direction based on the pointers if unified virtual addressing is active, but performance is optimized when the correct `hipMemcpyKind` is specified. Under the hood, it may use synchronous SDMA engine transfers or host-side mapping.

## Example
```cpp
#include <hip/hip_runtime.h>
#include <vector>

int main() {
    size_t N = 256;
    size_t bytes = N * sizeof(float);
    std::vector<float> h_A(N, 1.0f);
    float* d_A;
    
    hipMalloc(&d_A, bytes);
    // Host to Device
    hipMemcpy(d_A, h_A.data(), bytes, hipMemcpyHostToDevice);
    
    // Device to Host
    hipMemcpy(h_A.data(), d_A, bytes, hipMemcpyDeviceToHost);
    
    hipFree(d_A);
    return 0;
}
```
