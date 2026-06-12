---
name: hip-hipuserobjectcreate
description: "Create an instance of userObject to manage lifetime of a resource."
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

# hipUserObjectCreate

Create an instance of userObject to manage lifetime of a resource.

## Signature

```c
hipError_t hipUserObjectCreate(hipUserObject_t *object_out, void *ptr, hipHostFn_t destroy, unsigned int initialRefcount, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `object_out` | - pointer to instace of userobj. |
| [in] | `ptr` | - pointer to pass to destroy function. |
| [in] | `destroy` | - destroy callback to remove resource. |
| [in] | `initialRefcount` | - reference to resource. |
| [in] | `flags` | - flags passed to API. |

## Returns

hipSuccess , hipErrorInvalidValue

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___graph.html#ga0c464e200034254c80cdfb9277a55cb5)
