---
name: hip-hipmalloc
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

# hipMalloc

Allocate memory on the default accelerator.

## Signature

```c
hipError_t hipMalloc(void **ptr, size_t size);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | Pointer to the allocated memory |
| [in] | `size` | Requested memory size |

## Returns

hipSuccess , hipErrorOutOfMemory , hipErrorInvalidValue (bad context, null *ptr)

## Notes

- If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.

## See Also

- hipMallocPitch

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga4c6fcfe80010069d2792780d00dcead2)

## Semantics
Allocates memory on the device (GPU). Under the hood, it interacts with the AMD HSA/ROCr runtime to allocate a region of global memory and map it to the GPU's virtual address space. This memory is typically unpageable and resides in the GPU's high-bandwidth VRAM.

## Example
```cpp
#include <hip/hip_runtime.h>
#include <iostream>

int main() {
    float* d_A;
    size_t bytes = 1024 * sizeof(float);
    
    hipError_t err = hipMalloc(&d_A, bytes);
    if (err != hipSuccess) {
        std::cerr << "hipMalloc failed: " << hipGetErrorString(err) << std::endl;
        return -1;
    }
    
    // Free memory
    hipFree(d_A);
    return 0;
}
```
