---
name: hip-hipeventcreate
description: "Create an event"
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
  symbol_kind: function
  hw_unit: driver
  api_module: Event Management
---

# hipEventCreate

Create an event

## Signature

```c
hipError_t hipEventCreate(hipEvent_t *event);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in,out] | `event` | Returns the newly created event. |

## Returns

hipSuccess , hipErrorNotInitialized , hipErrorInvalidValue , hipErrorLaunchFailure , hipErrorOutOfMemory

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___event.html#ga5df2309c9f29ca4c8e669db658d411b4)

## Semantics
Creates a HIP event object. An event is used for timing or synchronization. It allocates an HSA signal (or analogous structure) that can track a specific point in a stream's execution.

## Example
```cpp
#include <hip/hip_runtime.h>

int main() {
    hipEvent_t event;
    hipEventCreate(&event);
    hipEventDestroy(event);
    return 0;
}
```
