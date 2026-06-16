---
name: triton-gdc-launch
description: Grid-dependent control — signal that the next kernel can launch
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,cuda,gdc,programmatic-dependency
---

# tl.extra.cuda.gdc_launch_dependents

Signal that the next kernel in a programmatic dependent launch chain can start executing.

## Syntax

```python
tl.extra.cuda.gdc_launch_dependents()
```

## Description

Part of the Grid-Dependent Control (GDC) API. When using programmatic dependent launch, this operation signals that the next program (kernel) can begin execution after all program instances in the current kernel have called this function or completed. This enables fine-grained kernel chaining without CPU involvement.

## Hardware Unit

Command Processor / Global Barrier

## Parameters

None

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper with programmatic dependent launch)

## Related Instructions

- [tl.extra.cuda.gdc_wait](../triton-gdc-wait/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def chained_kernel(x_ptr, sem_ptr, N, BLOCK: tl.constexpr):
    # Wait for prior kernel
    tl.extra.cuda.gdc_wait()

    # ... do work ...

    # Signal that this kernel is done; next kernel can launch
    tl.extra.cuda.gdc_launch_dependents()
```