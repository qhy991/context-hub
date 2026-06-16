---
name: triton-gluon-mbarrier
description: Mbarrier (memory barrier) for TMA synchronization in Hopper SM (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,mbarrier,sync,hopper
---

# tl.gluon.nvidia.hopper.mbarrier

Mbarrier (memory barrier) primitives for TMA synchronization on Hopper SM.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import mbarrier

# Core operations
mbarrier.allocate_mbarrier()
mbarrier.init(barrier, num_threads)
mbarrier.expect(barrier, bytes_per_cta)
mbarrier.arrive(barrier, count=1, pred=True)
mbarrier.wait(barrier)
mbarrier.invalidate(barrier)
```

## Description

Mbarrier is the synchronization primitive used with TMA on Hopper GPUs. Threads call `arrive()` to signal data production, and `wait()` to block until the expected data has arrived. The `expect()` call configures the expected byte count, and `init()` sets the initial state. Each TMA copy operation is associated with an mbarrier to coordinate the asynchronous data transfer.

## Operations

| Function | Description |
|----------|-------------|
| `allocate_mbarrier()` | Allocate a new mbarrier in shared memory |
| `init(barrier, num_threads)` | Initialize mbarrier for `num_threads` participants |
| `expect(barrier, bytes_per_cta)` | Set the expected byte count before arrival |
| `arrive(barrier, count, pred)` | Signal arrival (producer-side) |
| `wait(barrier)` | Block until all expected arrivals complete (consumer-side) |
| `invalidate(barrier)` | Invalidate the mbarrier for reuse |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_load](../triton-gluon-tma-async-load/DOC.md)
- [cluster.barrier](../triton-gluon-cluster-barrier/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma, mbarrier

# Allocate and initialize mbarrier
barrier = mbarrier.allocate_mbarrier()
mbarrier.init(barrier, num_threads=128)

# Signal expected data size
mbarrier.expect(barrier, bytes_per_cta=BLOCK_M * BLOCK_K * 2)  # fp16 = 2 bytes

# Async TMA load with barrier
tma.async_load(a_desc, [offs_am, offs_k], barrier, shared_buf)

# Wait for TMA to complete
mbarrier.wait(barrier)

# Now safe to use shared_buf
result = tl.dot(shared_buf, b)
```