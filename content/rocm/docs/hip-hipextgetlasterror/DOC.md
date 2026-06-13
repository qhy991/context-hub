---
name: hip-hipextgetlasterror
description: "Return last error returned by any HIP runtime API call and resets the stored error code to hipSuccess ."
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
  symbol_kind: function
  hw_unit: driver
  api_module: Error Handling
---

# hipExtGetLastError

Return last error returned by any HIP runtime API call and resets the stored error code to hipSuccess .

## Signature

```c
hipError_t hipExtGetLastError(void);
```

## Returns

return code from last HIP called from the active host thread

## Notes

- Returns the last error that has been returned by any of the runtime calls in the same host thread, and then resets the saved error to hipSuccess .

## See Also

- hipError_t

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___error.html#ga8dd52a2fe779f9b23a3e8c64a3a320a1)
