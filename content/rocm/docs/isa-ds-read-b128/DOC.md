---
name: isa-ds-read-b128
description: "Load 128 bits of data from a data share into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_READ_B128

Load 128 bits of data from a data share into a vector register.

## Encoding

Encoding: `ENC_DS`
Opcode: `255`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 128bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 128bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Reads 128 bits (4 dwords) from Local Data Share (LDS). Extremely useful for vectorized memory loads from shared memory in matrix multiplication and AI kernels to maximize bandwidth.

## Example
```cpp
__device__ float4 read_lds_128(uint32_t lds_offset) {
    float4 val;
    asm volatile(
        "ds_read_b128 %0, %1 offset:0" 
        : "=v"(val) : "v"(lds_offset)
    );
    return val;
}
```
