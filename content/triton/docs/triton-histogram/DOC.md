---
name: triton-histogram
description: Compute histogram of tensor values into bins
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,histogram,statistics
---

# tl.histogram

Computes a histogram of the values in `input` into `num_bins` equally spaced bins between `min_val` and `max_val`. Each element is atomically accumulated into its corresponding bin. This is commonly used for data distribution analysis and quantile computation.

## Syntax

```python
tl.histogram(input, num_bins, min_val, max_val)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| num_bins | int | Number of histogram bins |
| min_val | float | Lower bound of the histogram range |
| max_val | float | Upper bound of the histogram range |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor of size `num_bins` with bin counts |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_add](../triton-atomic-add/DOC.md)
- [tl.gather](../triton-gather/DOC.md)

## Example

```python
import triton.language as tl

counts = tl.histogram(data, num_bins=256, min_val=0.0, max_val=1.0)
```
