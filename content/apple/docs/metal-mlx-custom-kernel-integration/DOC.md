---
name: metal-mlx-custom-kernel-integration
description: "Wrapping custom Metal kernels into Apple's MLX Python framework: C++ bindings, MLX streams, and array handling natively."
metadata:
  languages: "cpp"
  versions: "4.0"
  revision: 1
  updated-on: "2026-03-22"
  source: official
  tags: "apple,metal,mlx,python,cpp,extension,custom-kernel,custom-op,stream,array"
---

# Metal & MLX Custom Kernel Integration

Use this page to integrate highly optimized custom Metal Shading Language (`.metal`) code into Apple's MLX machine learning framework.

## Why MLX over PyTorch on Mac?

While PyTorch's MPS backend is excellent, MLX is purpose-built by Apple for Apple Silicon. 
- MLX uses unified memory implicitly (no explicit `.to("mps")` calls).
- MLX allows lazy evaluation and graph compilation.
- MLX custom C++ extensions are drastically simpler to write and bind than PyTorch ATen extensions.

## Core Integration Structure

To build a custom operation in MLX, you need three components:
1. The `.metal` shader file containing the compute kernel.
2. A C++ header/source file using `mlx/mlx.h` to allocate outputs and dispatch the kernel onto the Metal command queue.
3. A Python wrapper (via `nanobind` or `pybind11`).

## Managing the MLX Stream

MLX handles its own Metal Command Queues via the `mlx::core::Stream` abstraction.
**Rule:** Never create a new `MTLCommandQueue` inside your extension. Always extract it from MLX's current stream.

```cpp
#include <mlx/mlx.h>
#include <mlx/backend/metal/metal.h>

using namespace mlx::core;

void my_custom_kernel_eval(const array& input, array& output) {
    // 1. Get the Metal device and command queue from MLX
    auto& d = metal::device(mlx::core::Device::gpu);
    MTLCommandQueue* queue = d.queue();
    MTLCommandBuffer* command_buffer = d.get_command_buffer(stream());
    
    // 2. Extract pipeline state (compile from source or library)
    id<MTLComputePipelineState> pso = d.get_kernel("my_metal_kernel");
    
    // 3. Encode the compute command
    id<MTLComputeCommandEncoder> encoder = [command_buffer computeCommandEncoder];
    [encoder setComputePipelineState:pso];
    [encoder setBuffer:static_cast<MTLBuffer*>(input.data()) offset:0 atIndex:0];
    [encoder setBuffer:static_cast<MTLBuffer*>(output.data()) offset:0 atIndex:1];
    
    // 4. Dispatch
    MTLSize grid = MTLSizeMake(input.size(), 1, 1);
    MTLSize threadgroup = MTLSizeMake(256, 1, 1);
    [encoder dispatchThreads:grid threadsPerThreadgroup:threadgroup];
    [encoder endEncoding];
}
```

## Array Contiguity and Data Pointers

Just like in PyTorch, you must verify the MLX `array` memory layout before casting it to an `MTLBuffer`:
- Use `input.flags().contiguous` to check if a tensor is contiguous.
- If not, you either pass the strides to the Metal kernel via a struct buffer and compute `index = compute_strided_idx(...)` inside the kernel, or you force contiguity on the C++ side using `mlx::core::reshape`.

## JIT Compilation vs Pre-compiled Libraries

- **Pre-compiled `.metallib`:** Faster load times. Good for production. You must package the `.metallib` next to your Python module.
- **JIT Compilation (`metal::device::get_kernel` from source string):** Excellent for auto-tuning, runtime dimensionality hardcoding, and Agent-generated code.

## Related Topics

- Metal PyTorch Custom Op Patterns: `../metal-pytorch-custom-op-host-patterns/DOC.md`

## Official Source Links (Fact Check)

- Apple MLX Framework Repository: https://github.com/ml-explore/mlx
- MLX Custom Extension tutorial: https://ml-explore.github.io/mlx/build/html/usage/custom_extensions.html

Last cross-check date: 2026-03-22
