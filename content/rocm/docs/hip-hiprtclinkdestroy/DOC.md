---
name: hip-hiprtclinkdestroy
description: "Deletes the link instance via hiprtc APIs."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,runtime-compilation
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Runtime Compilation
---

# hiprtcLinkDestroy

Deletes the link instance via hiprtc APIs.

## Signature

```c
hipError_t hiprtcLinkDestroy(hiprtcLinkState hip_link_state);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `hip_link_state` | link state instance |

## Returns

HIPRTC_SUCCESS

## See Also

- hiprtcResult

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___runtime.html#ga472583d0d93fa14458171969ae726c24)
