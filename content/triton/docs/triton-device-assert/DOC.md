---
name: triton-device-assert
description: Runtime assertion from device code
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,debug,assert
---

# tl.device_assert

Assert a condition at runtime from device code.

## Syntax

```python
tl.device_assert(condition, message="")
```

## Description

Asserts that `condition` is true on the GPU. If the assertion fails, the kernel terminates with an error message. This is a debugging tool — it has performance overhead and should be removed in production kernels. Similar to CUDA's `assert()`.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| condition | bool | Condition to check |
| message | str (optional) | Error message on failure |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.debug_barrier](../triton-debug-barrier/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def safe_div_kernel(a_ptr, b_ptr, out_ptr, N, BLOCK: tl.constexpr):
    offsets = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    a = tl.load(a_ptr + offsets, mask=mask)
    b = tl.load(b_ptr + offsets, mask=mask)

    # Ensure no division by zero
    tl.device_assert(b != 0, "Division by zero detected!")

    tl.store(out_ptr + offsets, a / b, mask=mask)
```