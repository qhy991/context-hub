---
name: hip-hipstreamsetattribute
description: "Sets stream attribute. Updated attribute is applied to work submitted to the stream."
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

# hipStreamSetAttribute

Sets stream attribute. Updated attribute is applied to work submitted to the stream.

## Signature

```c
hipError_t hipStreamSetAttribute(hipStream_t stream, hipStreamAttrID attr, const hipStreamAttrValue *value);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream to set attributes to |
| [in] | `attr` | - Attribute ID for the attribute to set |
| [in] | `value` | - Attribute value for the attribute to set |

## Returns

hipSuccess , hipErrorInvalidValue , hipErrorInvalidResourceHandle

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gac1aa936620145bf822f0318a9ac758c2)
