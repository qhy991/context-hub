---
name: triton-tensor-desc-class
description: Host-side TensorDescriptor for TMA kernel arguments (SM 9.0+)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,tma,descriptor,host,hopper
---

# triton.tools.tensor_descriptor.TensorDescriptor

Host-side descriptor class for passing TMA-capable tensor arguments to kernels.

## Syntax

```python
from triton.tools.tensor_descriptor import TensorDescriptor

desc = TensorDescriptor(base, shape, strides, block_shape, padding="zero", round_f32_to_tf32=False)
# or
desc = TensorDescriptor.from_tensor(tensor, block_shape, padding="zero", round_f32_to_tf32=False)
```

## Description

`TensorDescriptor` is a host-side Python class that wraps a tensor with TMA metadata. It is passed as a kernel argument instead of a raw pointer. When the kernel calls `desc.load()` or `desc.store()`, Triton emits TMA instructions for hardware-accelerated data movement on Hopper+ GPUs. This enables persistent kernel patterns where a single thread block processes multiple tiles via asynchronous TMA copy.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| base | torch.Tensor | Underlying tensor |
| shape | List[int] | Tensor shape |
| strides | List[int] | Tensor strides |
| block_shape | List[int] | Tile shape for TMA load/store |
| padding | str | Padding mode: `"zero"` (default) |
| round_f32_to_tf32 | bool | Whether to round fp32 to tf32 (default False) |

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [tl.make_tensor_descriptor](../triton-make-tensor-descriptor/DOC.md)
- [tl.load_tensor_descriptor](../triton-load-tensor-desc/DOC.md)

## Example

```python
import torch
import triton
from triton.tools.tensor_descriptor import TensorDescriptor

# Host-side: create descriptor from tensor
a = torch.randn(M, K, dtype=torch.float16, device='cuda')
b = torch.randn(K, N, dtype=torch.float16, device='cuda')
c = torch.empty(M, N, dtype=torch.float16, device='cuda')

a_desc = TensorDescriptor.from_tensor(a, [BLOCK_M, BLOCK_K])
b_desc = TensorDescriptor.from_tensor(b, [BLOCK_K, BLOCK_N])
c_desc = TensorDescriptor.from_tensor(c, [BLOCK_M, BLOCK_N])

# Launch kernel with descriptors
grid = lambda meta: (triton.cdiv(M, meta['BLOCK_M']),
                     triton.cdiv(N, meta['BLOCK_N']))
kernel[grid](a_desc, b_desc, c_desc, M, N, K)
```