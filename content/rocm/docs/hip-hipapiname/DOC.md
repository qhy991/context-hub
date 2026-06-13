---
name: hip-hipapiname
description: "Returns HIP API name by ID."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,callback-activity-apis
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Callback Activity APIs
---

# hipApiName

Returns HIP API name by ID.

## Signature

```c
hipError_t hipApiName(uint32_t id);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `id` | ID of HIP API |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___callback.html#ga3400d5eaec7294a79b98f3bd465adc3a)
