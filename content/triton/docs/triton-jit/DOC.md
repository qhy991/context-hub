---
name: triton-jit
description: JIT-compile a Python function into a GPU kernel
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,jit,kernel,programming-model
---

# triton.jit

Decorator for JIT-compiling a Python function using the Triton compiler.

## Syntax

```python
@triton.jit
def kernel_fn(args, ...):
    ...

# or with options
@triton.jit(debug=True, noinline=False)
def kernel_fn(args, ...):
    ...
```

## Description

`triton.jit` compiles a Python function into PTX/ROCm GPU code at call time. The decorated function becomes a `JITFunction` that can be launched with a grid tuple. When a JIT function is called, arguments with `.data_ptr()` and `.dtype` are implicitly converted to pointers. The compiled function can only access: Python primitives, builtins from the triton package, function arguments, and other `@triton.jit`-decorated functions.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| fn | Callable | Function to JIT-compile |
| version | str (optional) | Triton version target |
| debug | bool (optional) | Enable debug info in compiled kernel |
| noinline | bool (optional) | Prevent inlining of this function |
| do_not_specialize | Iterable[int\|str] | Argument names/indices to not specialize on |
| do_not_specialize_on_alignment | Iterable[int\|str] | Arguments to not specialize on alignment |

## Launch Convention

```python
kernel_fn[(grid_x, grid_y, grid_z)](args, ..., num_warps=4, num_stages=2)
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+), Intel GPU

## Related Instructions

- [triton.autotune](../triton-autotune/DOC.md)
- [triton.Config](../triton-config/DOC.md)

## Example

```python
import triton
import triton.language as tl

@triton.jit
def add_kernel(x_ptr, y_ptr, out_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    tl.store(out_ptr + offsets, x + y, mask=mask)

# Launch kernel
add_kernel[(grid_size,)](x, y, out, N, BLOCK=1024)
```