---
name: metal-w4a16-quantization-unpacking
description: "W4A16 weight-only quantization on Apple Silicon: fast inner-loop decompression using Bitwise ops, sub-byte packing, and Unified Memory scaling."
metadata:
  languages: "cpp"
  versions: "4.0"
  revision: 1
  updated-on: "2026-03-22"
  source: official
  tags: "apple,metal,w4a16,quantization,awq,int4,unpacking,memory-bound,llm"
---

# Metal W4A16 Quantization Unpacking

Use this page to design memory-efficient Metal decoding kernels that store LLM weights in 4-bit integers but execute arithmetic in Float16/BFloat16.

## The INT4 Reality on M-Series

Unlike modern NVIDIA hardware which has native mixed-precision MMA instructions for W4A16, Apple's AMX coprocessor (via `simdgroup_matrix`) specifically operates on natively supported sizes (Float16, Float32).

To achieve the bandwidth savings of INT4 without crippling compute:
1. Load packed 4-bit weights from the Unified Memory in 32-bit `uint` chunks.
2. Manually "unpack" them in the inner loop using fast ALU bitwise operations within the SIMD-group.
3. Convert to `half`, apply the group Scale/ZeroPoint, and load into a `simdgroup_matrix`.

## Unpacking Strategy in MSL

Since Metal Shading Language is C++14 based, standard bit manipulation is available, but you must ensure it does not generate slow branch-heavy assembly.

- **Storage:** Pack eight 4-bit weights into one `uint`.
- **Extraction:**
  ```cpp
  uint packed_val = weight_ptr[idx];
  // Extract 4-bit element at position 'p'
  uint extracted = (packed_val >> (p * 4)) & 0xF;
  ```
- **Vectorization:** Use Metal's native vector types (like `half8`, `uint4`) to load 128-bit caches and unpack them continuously. Vectorizing operations over `half4` drastically reduces the instruction count compared to scalar shifts.

## The Dequantization Math

For AWQ-style quantization ($W_{fp16} = (W_{int4} - ZP) \times Scale$):
- You must manage "Groups" (usually 64 or 128 weights per scale).
- Do not let the Scale / ZeroPoint reload become a new memory bottleneck. Load the single `half` scale and `half` zero point into a SIMD-group register and broadcast it across the 64-unpacked weights during the conversion phase.

## UMA Advantage in Quantization

Because Apple Silicon uses Unified Memory (UMA):
- You do not need a complex host-to-device packing/unpacking pipeline just to move the model onto the GPU. 
- You can map the `.safetensors` file containing the INT4 weights directly into memory and point the Metal kernel to it instantly.

## Related Topics

- Metal Unified Memory Optimization: `../metal-unified-memory-uma-optimization/DOC.md`
- Metal SIMD-group AMX Playbook: `../metal-simdgroup-matrix-amx-playbook/DOC.md`

## Official Source Links (Fact Check)

- Apple MLX Framework (Quantized Matmul implementations): https://github.com/ml-explore/mlx
- Metal Shading Language: https://developer.apple.com/metal/resources/

Last cross-check date: 2026-03-22
