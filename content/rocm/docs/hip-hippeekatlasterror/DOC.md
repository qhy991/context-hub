---
name: hip-hippeekatlasterror
description: "Return last error returned by any HIP runtime API call."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,error-handling
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Error Handling
---

# hipPeekAtLastError

Return last error returned by any HIP runtime API call.

## Signature

```c
hipError_t hipPeekAtLastError(void);
```

## Returns

hipSuccess

## Notes

- Returns the last error that has been returned by any of the runtime calls in the same host thread. Unlike hipGetLastError, this function does not reset the saved error code.

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___error.html#ga1dd660bc739f7e13edd34615660f0148)
