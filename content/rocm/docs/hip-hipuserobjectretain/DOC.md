---
name: hip-hipuserobjectretain
description: "Retain number of references to resource."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,graph-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Graph Management
---

# hipUserObjectRetain

Retain number of references to resource.

## Signature

```c
hipError_t hipUserObjectRetain(hipUserObject_t object, unsigned int count);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `object` | - pointer to instace of userobj. |
| [in] | `count` | - reference to resource to be retained. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga87b191d080e9b6c9d1ec1bc7990e405d)
