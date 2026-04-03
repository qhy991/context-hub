---
name: metal-unified-memory-uma-optimization
description: "Apple Silicon Unified Memory Architecture (UMA) for LLMs: zero-copy CPU-GPU data sharing, MTLStorageModeShared, and KV cache handling."
metadata:
  languages: "cpp"
  versions: "4.0"
  revision: 1
  updated-on: "2026-03-22"
  source: official
  tags: "apple,metal,uma,unified-memory,zero-copy,mtlstoragemodeshared,kv-cache,llm,memory-bandwidth"
---

# Metal Unified Memory Architecture (UMA) Optimization

Use this page to architect Metal memory allocations for Large Language Models (LLMs), taking full advantage of Apple Silicon's unique Unified Memory Architecture.

## The PCIe Bottleneck Does Not Exist

On traditional discrete GPUs (NVIDIA/AMD), system RAM and VRAM are physically separated by a PCIe bus. Moving data between them is extremely slow ($\sim 32-64$ GB/s).
On Apple Silicon (M1/M2/M3/M4 Max/Ultra), the CPU, GPU, and Neural Engine share the exact same physical LPDDR5 memory pool ($\sim 400-800$ GB/s).

## Zero-Copy Buffers: `MTLStorageModeShared`

For dynamic data that the CPU needs to read/write constantly (like the generation sequence in an LLM or dynamic KV cache metadata), **do not use `MTLStorageModePrivate` and explicit blit copies.**

Instead, allocate the buffer identically on both sides using `MTLStorageModeShared`.
```objective-c
id<MTLBuffer> buffer = [device newBufferWithLength:size 
                                           options:MTLResourceStorageModeShared];
// CPU writes directly
float* cpu_ptr = (float*)buffer.contents;
cpu_ptr[0] = 1.0f;
// GPU reads directly without any copy overhead!
```

## KV Cache Management

Because of UMA, you have a massive advantage for long-context LLMs:
- A 128GB Mac Studio can effectively use ~100GB as pure VRAM for KV Cache.
- **KV CPU Offloading is obsolete:** On NVIDIA, "offloading to CPU" means transferring over PCIe. On Apple Silicon, "offloading to CPU RAM" just means the GPU accesses the exact same physical RAM array, maintaining massive bandwidth. 
- You can treat the entire Unified Memory as one giant Paged Attention Block Table.

## When to use `MTLStorageModePrivate`

For static model weights that the CPU loads once from disk and never touches again, `MTLStorageModePrivate` allows the Metal driver to perform micro-optimizations (like specific cache-line alignments or compression) tailored exclusively for the GPU.

*Workflow for Weights:*
1. Create a `Shared` buffer.
2. `mmap` the `.safetensors` file into the `Shared` buffer.
3. Create a `Private` buffer.
4. Execute an `MTLBlitCommandEncoder` to copy from Shared to Private.

## Cache Coherency and Synchronization

While Unified Memory is shared, the CPU and GPU have separate L1/L2 caches.
- If the CPU modifies a `Shared` buffer while a Metal compute kernel is in flight, the GPU might read stale data.
- **Rule of thumb:** Always use `MTLEvent` or `MTLSharedEvent` to block the CPU from touching memory until the GPU command buffer signals completion.

## Related Topics

- Metal Memory and Threadgroup: `../metal-memory-and-threadgroup/DOC.md`
- Metal Heaps, Fences, and Events: `../metal-heaps-fences-and-events/DOC.md`

## Official Source Links (Fact Check)

- Apple Developer: Synchronizing a Managed Buffer: https://developer.apple.com/documentation/metal/resource_fundamentals/synchronizing_a_managed_buffer
- Setting Resource Storage Modes: https://developer.apple.com/documentation/metal/setting_resource_storage_modes

Last cross-check date: 2026-03-22
