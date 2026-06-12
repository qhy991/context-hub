---
name: hip-hipsetdeviceflags
description: "The current device behavior is changed according to the flags passed."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,device-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Device Management
---

# hipSetDeviceFlags

The current device behavior is changed according to the flags passed.

## Signature

```c
hipError_t hipSetDeviceFlags(unsigned flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `flags` | Flag to set on the current device |

## Returns

hipSuccess , hipErrorNoDevice , hipErrorInvalidDevice , hipErrorSetOnActiveProcess

## Notes

- The schedule flags impact how HIP waits for the completion of a command running on a device.
- hipDeviceScheduleSpin : HIP runtime will actively spin in the thread which submitted the work until the command completes. This offers the lowest latency, but will consume a CPU core and may increase power.
- hipDeviceScheduleYield : The HIP runtime will yield the CPU to system so that other tasks can use it. This may increase latency to detect the completion but will consume less power and is friendlier to other tasks in the system.
- hipDeviceScheduleBlockingSync : On ROCm platform, this is a synonym for hipDeviceScheduleYield.
- hipDeviceScheduleAuto : This is the default value if the input 'flags' is zero. Uses a heuristic to select between Spin and Yield modes. If the number of HIP contexts is greater than the number of logical processors in the system, uses Spin scheduling, otherwise uses Yield scheduling.
- hipDeviceMapHost : Allows mapping host memory. On ROCm, this is always allowed and the flag is ignored.
- hipDeviceLmemResizeToMax : This flag is silently ignored on ROCm.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#ga6e54db382768827e84725632018307aa)
