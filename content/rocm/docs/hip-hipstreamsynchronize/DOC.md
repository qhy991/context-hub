---
name: hip-hipstreamsynchronize
description: "Waits for all commands in the stream to complete."
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

# hipStreamSynchronize

Waits for all commands in the stream to complete.

## Signature

```c
hipError_t hipStreamSynchronize(hipStream_t stream);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `stream` | Stream identifier. |

## Returns

hipSuccess , hipErrorInvalidHandle

## Notes

- This command is host-synchronous : the host will block until all operations on the specified stream with its associated device are completed. On multiple device systems, the stream is associated with its device, no need to call hipSetDevice before this API.
- This command follows standard null-stream semantics. Specifying the null stream will cause the command to wait for other streams on the same device to complete all pending operations.
- This command honors the hipDeviceScheduleBlockingSync flag, which controls whether the wait is active or blocking.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html#gabbfb9f573a6ebe8c478605ecb5504a74)
