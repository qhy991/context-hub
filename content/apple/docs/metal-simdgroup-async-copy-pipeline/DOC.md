---
name: metal-simdgroup-async-copy-pipeline
description: "Async copy and double buffering in Metal: avoiding global memory pipeline stalls with simdgroup_async_copy from Device to Threadgroup."
metadata:
  languages: "cpp"
  versions: "4.0"
  revision: 1
  updated-on: "2026-03-22"
  source: official
  tags: "apple,metal,async-copy,pipeline,double-buffering,prefetch,simdgroup_async_copy,threadgroup"
---

# Metal SIMD-group Async Copy Pipeline

Use this page to implement asynchronous global-to-shared memory transfers in Metal (Metal 3+), mimicking the pipeline advantages of CUDA's `cp.async`.

## The Sync-Wait Bottleneck

In older Metal kernels (or naive GEMM implementations), threads execute `load`, then wait for data to reach registers, write it to `threadgroup` (shared) memory, synchronize, and then compute. 
This serializes memory fetching and arithmetic operations, leaving the ALU (AMX) idle during global memory latency.

## `simdgroup_async_copy`

Starting with Metal 3, Apple Silicon supports asynchronous copy directly from `device` memory to `threadgroup` memory. 

- This instruction bypasses the need to load data into thread registers first.
- The SIMD-group issues the command and can immediately proceed to perform unrelated math (e.g., computing on the *previous* tile) while the memory subsystem fulfills the copy in the background.

```cpp
#include <metal_stdlib>
using namespace metal;

// 1. Issue the copy for the NEXT tile
simdgroup_event copy_event;
copy_event = simdgroup_async_copy(dst_threadgroup, src_device, elements, copy_event);

// 2. Wait for the copy to finish before using it
simdgroup_event::wait(1, &copy_event);
threadgroup_barrier(mem_flags::mem_threadgroup);
```

## Software Pipelining (Double Buffering)

To completely hide memory latency, allocate **two** buffers in `threadgroup` memory for your tiles ($A_{ping}, A_{pong}$ and $B_{ping}, B_{pong}$).

**The Prefetch Loop:**
1. Async fetch Tile 0 into Buffer 0.
2. Wait for Tile 0.
3. *Loop begins:*
   a. Async fetch Tile $N+1$ into Buffer 1 (background).
   b. Load `simdgroup_matrix` from Buffer 0 and execute Math (foreground).
   c. Wait for Tile $N+1$.
   d. Swap ping/pong pointers.

## Stride Limitations

Unlike CUDA TMA, `simdgroup_async_copy` expects a continuous block of memory. 
- If the matrix has a stride (i.e., a row width larger than the tile width), you cannot just issue one block copy. 
- You must loop over the rows and issue multiple small asynchronous copies per SIMD-group, accumulating the events.

## Related Topics

- Metal Tiled Matmul Patterns: `../metal-tiled-matmul-patterns/DOC.md`
- Metal SIMD-group AMX Playbook: `../metal-simdgroup-matrix-amx-playbook/DOC.md`

## Official Source Links (Fact Check)

- Metal Shading Language Specification (Asynchronous copy functions): https://developer.apple.com/metal/resources/
- Translating CUDA to Metal (Apple WWDC): https://developer.apple.com/videos/play/wwdc2022/10103/

Last cross-check date: 2026-03-22
