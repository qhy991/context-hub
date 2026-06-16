---
name: triton-gluon-cluster-barrier
description: Cluster-wide barrier for multi-CTA synchronization (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,cluster,barrier,sync,hopper
---

# tl.gluon.nvidia.hopper.cluster

Cluster-level barrier primitives for multi-CTA synchronization.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import cluster

# Core operations
cluster.arrive(relaxed=False)
cluster.wait()
cluster.barrier(relaxed=False)
```

## Description

Provides cluster-wide synchronization primitives for Hopper GPUs. A cluster is a group of CTAs (Cooperative Thread Arrays) that can share data through shared memory and coordinate via cluster barriers. `cluster.barrier()` combines `arrive()` and `wait()` into a single call. `relaxed=True` trades some ordering guarantees for lower latency.

## Operations

| Function | Description |
|----------|-------------|
| `cluster.arrive(relaxed)` | Signal arrival at the cluster barrier |
| `cluster.wait()` | Block until all CTAs in the cluster have arrived |
| `cluster.barrier(relaxed)` | Combined arrive + wait (cluster-wide `__syncthreads`) |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [mbarrier](../triton-gluon-mbarrier/DOC.md)
- [tl.debug_barrier](../triton-debug-barrier/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import cluster

# Each CTA computes its partition
local_result = compute_partition(pid, data)

# Synchronize all CTAs in the cluster
cluster.barrier()

# Now safe to read results from other CTAs in shared memory
final_result = combine_results(local_result, shared_mem)
```