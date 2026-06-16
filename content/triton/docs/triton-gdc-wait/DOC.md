---
name: triton-gdc-wait
description: Grid-dependent control — wait for all prior kernel instructions to complete
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,cuda,gdc,programmatic-dependency
---

# tl.extra.cuda.gdc_wait

Blocking instruction that waits for all instructions in the previous kernel to complete before proceeding.

## Syntax

```python
tl.extra.cuda.gdc_wait()
```

## Description

Part of the Grid-Dependent Control (GDC) / Programmatic Dependent Launch API. This barrier ensures that all instructions from prior kernels have completed before the current kernel continues executing. Used together with `gdc_launch_dependents` to implement programmatic kernel launch chains where the next kernel depends on the current one.

## Hardware Unit

Command Processor / Global Barrier

## Parameters

None

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper with programmatic dependent launch)

## Related Instructions

- [tl.extra.cuda.gdc_launch_dependents](../triton-gdc-launch/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def producer_kernel(x_ptr, sem_ptr, N, BLOCK: tl.constexpr):
    # Wait for previous kernel to finish
    tl.extra.cuda.gdc_wait()
    # ... produce data ...
    tl.extra.cuda.gdc_launch_dependents()
```