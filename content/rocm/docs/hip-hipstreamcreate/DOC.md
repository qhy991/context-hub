---
name: hip-hipstreamcreate
description: "Creates an asynchronous stream."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Management
---

# hipStreamCreate

Creates an asynchronous stream.

## Signature

```c
hipError_t hipStreamCreate(hipStream_t *stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `stream` | Valid pointer to hipStream_t. This function writes the memory with the newly created stream. |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Creates a new asynchronous stream with its associated current device. The stream returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, the application must call hipStreamDestroy.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gaff5b62d6e9502d80879f7176f4d03102)

## Semantics
Creates an asynchronous execution stream. A stream corresponds to a hardware or software command queue in the ROCr runtime. Commands placed in the same stream execute strictly in order.

## Example
```cpp
#include <hip/hip_runtime.h>

int main() {
    hipStream_t stream;
    hipStreamCreate(&stream);
    
    // ... launch kernels on stream ...
    
    hipStreamDestroy(stream);
    return 0;
}
```
