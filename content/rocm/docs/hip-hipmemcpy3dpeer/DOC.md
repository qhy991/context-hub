---
name: hip-hipmemcpy3dpeer
description: "Performs 3D memory copies between devices This API is asynchronous with respect to host."
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
  hw_unit: driver
  api_module: Memory Management
---

# hipMemcpy3DPeer

Performs 3D memory copies between devices This API is asynchronous with respect to host.

## Signature

```c
hipError_t hipMemcpy3DPeer(hipMemcpy3DPeerParms *p);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `p` | - Parameters for memory copy |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidDevice

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga80d9b368037c9e80b4d5a6704580f652)
