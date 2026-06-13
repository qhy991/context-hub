---
name: hip-hiphccmodulelaunchkernel
description: "This HIP API is deprecated, please use hipExtModuleLaunchKernel() instead."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,execution-control
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Execution Control
---

# hipHccModuleLaunchKernel

This HIP API is deprecated, please use hipExtModuleLaunchKernel() instead.

## Signature

```c
hipError_t hipHccModuleLaunchKernel(hipFunction_t f, uint32_t globalWorkSizeX, uint32_t globalWorkSizeY, uint32_t globalWorkSizeZ, uint32_t localWorkSizeX, uint32_t localWorkSizeY, uint32_t localWorkSizeZ, size_t sharedMemBytes, hipStream_t hStream, void **kernelParams, void **extra, hipEvent_t startEvent, hipEvent_t stopEvent);
```

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___execution.html#ga0977a04384013028d822eb0c6b5cf901)
