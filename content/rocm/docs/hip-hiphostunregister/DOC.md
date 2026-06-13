---
name: hip-hiphostunregister
description: "Un-register host pointer."
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

# hipHostUnregister

Un-register host pointer.

## Signature

```c
hipError_t hipHostUnregister(void *hostPtr);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hostPtr` | Host pointer previously registered with hipHostRegister |

## Returns

Error code

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#ga4c9e1810b9f5858d36c4d28c91c86924)
