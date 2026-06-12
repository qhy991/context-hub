---
name: hip-hipMalloc
description: "Allocate device memory on the GPU. Fundamental HIP runtime API for GPU memory management, equivalent to cudaMalloc."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory,allocation
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
---

# hipMalloc

Allocate device memory on the GPU. Equivalent to `cudaMalloc`.

## Syntax

```c
hipError_t hipMalloc(void** ptr, size_t size);
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| ptr | void** | Pointer to allocated device memory |
| size | size_t | Number of bytes to allocate |
| **Return** | hipError_t | `hipSuccess` on success |

## Description

Allocates `size` bytes of linear memory on the device and returns a pointer in `*ptr`. The allocated memory is suitably aligned for any type.

## CUDA Equivalence

```c
// CUDA
cudaError_t err = cudaMalloc(&d_ptr, size);

// HIP (drop-in replacement)
hipError_t err = hipMalloc(&d_ptr, size);
```

## Example

```c
#include <hip/hip_runtime.h>

int main() {
    float* d_data;
    size_t size = 1024 * 1024 * sizeof(float);  // 1M floats

    hipError_t err = hipMalloc(&d_data, size);
    if (err != hipSuccess) {
        printf("hipMalloc failed: %s\n", hipGetErrorString(err));
        return -1;
    }

    // Use d_data...

    hipFree(d_data);
    return 0;
}
```

## Error Codes

| Error | Meaning |
|-------|---------|
| hipSuccess | Allocation successful |
| hipErrorMemoryAllocation | Allocation failed (out of memory) |
| hipErrorInvalidValue | Invalid argument (e.g., size=0) |

## See Also

- `hipFree` — Free device memory
- `hipMallocManaged` — Allocate unified memory
- `hipHostMalloc` — Allocate pinned host memory
- `hipMemcpy` — Copy memory between host and device

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
