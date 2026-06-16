---
name: triton-gluon-fence-async-shared
description: Fence to complete async shared memory operations (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,fence,async,shared-memory,hopper
---

# tl.gluon.nvidia.hopper.fence_async_shared

Issue a fence to complete asynchronous shared memory operations.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import fence_async_shared

fence_async_shared()
```

## Description

Emits a `fence.proxy.async` instruction that ensures all pending asynchronous shared memory operations (such as TMA copies) targeting shared memory are completed and visible. This is a hardware-level memory fence, stronger than `tl.debug_barrier()` for async operations. Must be called after `async_store` to shared memory to guarantee visibility.

## Hardware Unit

Memory Fence Unit

## Parameters

None

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_store](../triton-gluon-tma-async-store/DOC.md)
- [mbarrier](../triton-gluon-mbarrier/DOC.md)
- [tl.debug_barrier](../triton-debug-barrier/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import fence_async_shared

# Async store to shared memory
tma.async_store(dest_desc, [offs_dm, offs_dn], src_shared)

# Fence: ensure async store is visible to all threads
fence_async_shared()

# Now other threads can safely read from shared memory
tl.debug_barrier()
result = tl.load(shared_ptr)
```