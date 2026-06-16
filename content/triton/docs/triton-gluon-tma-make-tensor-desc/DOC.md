---
name: triton-gluon-tma-make-tensor-desc
description: Create a tensor descriptor for Gluon TMA operations (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,descriptor,hopper
---

# tl.gluon.nvidia.hopper.tma.make_tensor_descriptor

Create a tensor descriptor for low-level TMA operations in the Gluon experimental namespace.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

desc = tma.make_tensor_descriptor(base, shape, strides, block_shape, layout, padding_option="zero")
```

## Description

Creates a tensor descriptor object for use with low-level TMA APIs (`async_load`, `async_store`, etc.). Unlike the high-level `tl.make_tensor_descriptor`, this version requires an explicit `layout` parameter specifying the shared memory layout (e.g., `NVMMASharedLayout`, `PaddedSharedLayout`). This is the foundation for all TMA operations in the Gluon experimental namespace.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| base | tensor | Base pointer to the tensor in global memory |
| shape | List[tensor] | Shape of the full tensor |
| strides | List[tensor] | Strides of the full tensor |
| block_shape | List[constexpr] | Shape of the tile to load/store |
| layout | SharedLayout | Shared memory layout (NVMMASharedLayout, PaddedSharedLayout, etc.) |
| padding_option | str | Padding mode: `"zero"` (default) |

## Returns

| Type | Description |
|------|-------------|
| tensor_descriptor | Descriptor for use with `tma.async_load` / `tma.async_store` |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_load](../triton-gluon-tma-async-load/DOC.md)
- [async_store](../triton-gluon-tma-async-store/DOC.md)
- [tl.make_tensor_descriptor](../triton-make-tensor-descriptor/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma
from triton.experimental.gluon.language._layouts import NVMMASharedLayout

# Define shared memory layout
layout = NVMMASharedLayout(block_shape=[BLOCK_M, BLOCK_K])

# Create descriptor
a_desc = tma.make_tensor_descriptor(
    a_ptr,
    shape=[M, K],
    strides=[K, 1],
    block_shape=[BLOCK_M, BLOCK_K],
    layout=layout,
    padding_option="zero"
)
```