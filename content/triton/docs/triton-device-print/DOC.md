---
name: triton-device-print
description: Print values from device code at runtime (debug utility)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,debug,print,device
---

# tl.device-print

Prints values from the GPU device at runtime. Each call outputs a line with the given `prefix` string. Only the first thread in the first block prints by default.

## Syntax

```python
tl.device_print(prefix, *values)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| prefix | str | Label string for the output |
| *values | tensor | One or more values to print |

## Returns

| Type | Description |
|------|-------------|
| Block | None |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.device_print("x =", x)  # prints: x = [value]
```
