---
name: triton-gluon-tma-async-store-wait
description: Wait for pending TMA async stores to complete (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,store-wait,hopper
---

# tl.gluon.nvidia.hopper.tma.store_wait

Wait for pending TMA asynchronous stores to complete.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

tma.store_wait(pendings, read_only=True)
```

## Description

Blocks until the specified number of pending TMA store operations have completed. This is essential to call before a kernel exits if it has issued any `async_store` operations, to ensure all data is written back to global memory. `read_only=False` indicates stores that modify memory.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pendings | int | Number of pending operations to wait on |
| read_only | bool | Whether the stores are read-only (default True) |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_store](../triton-gluon-tma-async-store/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

# Issue async stores
tma.async_store(c_desc, [offs_cm, offs_cn], result)
tma.async_store(c_desc_2, [offs2_cm, offs2_cn], result2)

# Wait for both stores to complete before kernel exit
tma.store_wait(2)
```