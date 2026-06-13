---
name: hip-hipmoduleloaddata
description: "builds module from code object data which resides in host memory."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,module-management
  isa_category: runtime
  instruction_type: API
  symbol_kind: function
  hw_unit: driver
  api_module: Module Management
---

# hipModuleLoadData

builds module from code object data which resides in host memory.

## Signature

```c
hipError_t hipModuleLoadData(hipModule_t *module, const void *image);
```

## Parameters

| Direction | Parameter | Description |
|-----------|-----------|-------------|
| [in] | `image` | The pointer to the location of data |
| [out] | `module` | Retuned module |

## Returns

hipSuccess, hipErrorNotInitialized, hipErrorOutOfMemory, hipErrorNotInitialized

## Notes

- The "image" is a pointer to the location of code object data. This data can be either a single code object or a fat binary (fatbin), which serves as the entry point for loading and launching device-specific kernel executions.
- By default, the following command generates a fatbin:
- "amdclang++ -O3 -c --offload-device-only --offload-arch=&lt;GPU_ARCH&gt; &lt;input_file&gt; -o &lt;output_file&gt;"
- For more details, refer to: Kernel Compilation in the HIP kernel language C++ support, or HIP runtime compilation (HIP RTC) .

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___module.html#gaabdbd73e952a741e861d01109c4790f3)
