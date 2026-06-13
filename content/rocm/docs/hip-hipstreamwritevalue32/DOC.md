---
name: hip-hipstreamwritevalue32
description: "Enqueues a write command to the stream.[BETA]."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,stream-memory-operations
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Stream Memory Operations
---

# hipStreamWriteValue32

Enqueues a write command to the stream.[BETA].

## Signature

```c
hipError_t hipStreamWriteValue32(hipStream_t stream, void *ptr, uint32_t value, unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | - Stream identifier |
| [in] | `ptr` | - Pointer to a GPU accessible memory object |
| [in] | `value` | - Value to be written |
| [in] | `flags` | - reserved, ignored for now, will be used in future releases |

## Returns

hipSuccess , hipErrorInvalidValue

## Notes

- Enqueues a write command to the stream, write operation is performed after all earlier commands on this stream have completed the execution.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream_m.html#ga2520d4e1e57697edff2a85a3c03d652b)
