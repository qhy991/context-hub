---
name: isa-ds-read2st64-b64
description: "Local Data Share (LDS) paired read: reads two 64-bit values from LDS with stride-64 optimization. Critical for optimized matrix tile loads."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'GCN1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,lds,isa,memory,local-data-share,cdna
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
---

# ds_read2st64_b64

Read two 64-bit values from LDS (Local Data Share) with 64-element stride between them.

## Syntax

```asm
ds_read2st64_b64 v[4:5], v0  offset0:0  offset1:1
```

## Operands

| Operand | Type | Description |
|---------|------|-------------|
| v[dst:dst+1] | VGPR | Two 64-bit destination values |
| vaddr | VGPR | Base LDS address (in dwords) |
| offset0 | immediate | Offset to first read (0-255) |
| offset1 | immediate | Offset to second read (0-255), actual offset = offset1 * 64 |

## Description

Reads two 64-bit (2 dword) values from LDS in a single instruction:
- Value 0 from `vaddr + offset0 * 4`
- Value 1 from `vaddr + offset1 * 64 * 4`

The `st64` stride means the second read is offset by `64 * 4 = 256` bytes from the first. This is **optimized for accessing LDS with column-major patterns** where elements are 64 dwords apart.

## CUDA Equivalence

No direct CUDA equivalent — LDS operations are implicit in shared memory access patterns.

## HIP Usage

```c
// LDS is typically accessed via __shared__ memory
__shared__ float tile[256][64];

// Compiler generates DS instructions automatically
float val = tile[threadIdx.x][threadIdx.y];  // → ds_read_b32 or ds_read2_b64

// For explicit LDS control in inline asm:
asm volatile("ds_read2st64_b64 %0, %1 offset0:0 offset1:1"
    : "=v"(result) : "v"(lds_addr));
```

## Bank Conflict Avoidance

LDS has 64 banks (32 dwords per bank on CDNA):
- Each bank services one address per cycle
- `ds_read2` reads from two addresses simultaneously — **avoid both hitting same bank**
- Common fix: pad array dimensions by 1 dword to break bank conflicts

```c
// Bad: consecutive threads hit same banks
__shared__ float tile[64][64];

// Good: padding avoids bank conflicts
__shared__ float tile[64][65];  // +1 dword padding
```

## CDNA4 Enhancement: LDS Read-with-Transpose

CDNA4 introduces new LDS instructions that can **read and transpose** in one operation, eliminating the need for separate transpose kernels in GEMM epilogues.

## Performance

| Property | Value |
|----------|-------|
| LDS Size per CU | 64 KB (CDNA1-3), varies by arch |
| LDS Banks | 64 |
| Bank Width | 4 bytes (dword) |
| Latency | ~4-8 cycles |
| Throughput | 2 loads + 2 stores per cycle per CU |

## See Also

- `ds_read2_b64` — Non-stride paired read
- `ds_write2st64_b64` — Paired LDS write with stride
- `ds_read_b128` — 128-bit LDS read
- [AMDGPU Kernel Optimization Guide](https://github.com/nod-ai/shark-ai/blob/main/docs/amdgpu_kernel_optimization_guide.md)

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
