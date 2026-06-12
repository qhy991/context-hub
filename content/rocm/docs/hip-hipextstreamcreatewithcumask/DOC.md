---
name: hip-hipextstreamcreatewithcumask
description: "Creates an asynchronous stream with the specified CU mask."
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
  hw_unit: driver
  api_module: Stream Management
---

# hipExtStreamCreateWithCUMask

Creates an asynchronous stream with the specified CU mask.

## Signature

```c
hipError_t hipExtStreamCreateWithCUMask(hipStream_t *stream, uint32_t cuMaskSize, const uint32_t *cuMask);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `stream` | Pointer to new stream |
| [in] | `cuMaskSize` | Size of CU mask bit array passed in. |
| [in] | `cuMask` | Bit-vector representing the CU mask. Each active bit represents using one CU. The first 32 bits represent the first 32 CUs, and so on. If its size is greater than physical CU number (i.e., multiProcessorCount member of hipDeviceProp_t ), the extra elements are ignored. It is user's responsibility to make sure the input is meaningful. |

## Returns

hipSuccess , hipErrorInvalidHandle , hipErrorInvalidValue

## Notes

- Creates a new asynchronous stream with the specified CU mask. stream returns an opaque handle that can be used to reference the newly created stream in subsequent hipStream* commands. The stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope. To release the memory used by the stream, application must call hipStreamDestroy.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gad61df06555ebdfa30784b3233ca5e13f)
