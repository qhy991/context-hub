---
name: triton-inline-asm-elementwise
description: Execute inline PTX assembly element-wise on tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,asm,inline,ptx,advanced
---

# tl.inline-asm-elementwise

Executes inline PTX assembly element-wise. Advanced feature for using GPU instructions not exposed by Triton. `asm_template` is a PTX string with `$0`, `$1` placeholders. `constraints` specifies operand types ("=r" for output, "r" for input). `pack` groups elements for vector ops.

## Syntax

```python
tl.inline_asm_elementwise(asm_template, constraints, *args, dtype, is_pure=True, pack=1)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| asm_template | str | PTX assembly template |
| constraints | str | Operand constraints |
| *args | tensor | Operands |
| dtype | tl.dtype | Output dtype |
| is_pure | bool | No side effects (default True) |
| pack | int | Elements per thread (default 1) |

## Returns

| Type | Description |
|------|-------------|
| Block | Result of the inline assembly |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

x_fp16 = tl.inline_asm_elementwise(
    "cvt.rn.f16.f32 $0, $1;",
    "=r,r", x, dtype=tl.float16, is_pure=True, pack=1
)
```
