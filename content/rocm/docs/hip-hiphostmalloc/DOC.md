---
name: hip-hiphostmalloc
description: "Allocates device accessible page locked (pinned) host memory."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,memory-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Memory Management
---

# hipHostMalloc

Allocates device accessible page locked (pinned) host memory.

## Signature

```c
hipError_t hipHostMalloc(void **ptr, size_t size , unsigned int flags);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [out] | `ptr` | Pointer to the allocated host pinned memory |
| [in] | `size` | Requested memory size in bytes If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned. |
| [in] | `flags` | Type of host memory allocation. See the description of flags in hipSetDeviceFlags. |

## Returns

hipSuccess , hipErrorOutOfMemory

## Notes

- This API allocates pinned host memory which is mapped into the address space of all GPUs in the system, the memory can be accessed directly by the GPU device, and can be read or written with much higher bandwidth than pageable memory obtained with functions such as malloc().
- Using the pinned host memory, applications can implement faster data transfers for HostToDevice and DeviceToHost. The runtime tracks the hipHostMalloc allocations and can avoid some of the setup required for regular unpinned memory.
- When the memory accesses are infrequent, zero-copy memory can be a good choice, for coherent allocation. GPU can directly access the host memory over the CPU/GPU interconnect, without need to copy the data.
- Currently the allocation granularity is 4KB for the API.
- Developers need to choose proper allocation flag with consideration of synchronization.
- If no input for flags, it will be the default pinned memory allocation on the host.

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___memory.html#gaad40bc7d97ccc799403ef5a9a8c246e1)
