---
name: hip-hipeventcreatewithflags
description: "Create an event with the specified flags."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,event-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Event Management
---

# hipEventCreateWithFlags

Create an event with the specified flags.

## Signature

```c
hipError_t hipEventCreateWithFlags(hipEvent_t *event, unsigned flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `event` | Returns the newly created event. |
| [in] | `flags` | Flags to control event behavior. Valid values are hipEventDefault , hipEventBlockingSync , hipEventDisableTiming , hipEventInterprocess hipEventDefault : Default flag. The event will use active synchronization and will support timing. Blocking synchronization provides lowest possible latency at the expense of dedicating a CPU to poll on the event. hipEventBlockingSync : The event will use blocking synchronization : if hipEventSynchronize is called on this event, the thread will block until the event completes. This can increase latency for the synchroniation but can result in lower power and more resources for other CPU threads. hipEventDisableTiming : Disable recording of timing information. Events created with this flag would not record profiling data and provide best performance if used for synchronization. hipEventInterprocess : The event can be used as an interprocess event. hipEventDisableTiming flag also must be set when hipEventInterprocess flag is set. hipEventDisableSystemFence : Disable acquire and release system scope fence. This may improve performance but device memory may not be visible to the host and other devices if this flag is set. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue , hipErrorLaunchFailure , hipErrorOutOfMemory

## See Also

- hipEventCreate

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#gae86a5acb1b22b61bc9ecb9c28fc71b75)
