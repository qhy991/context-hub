---
name: isa-ds-write2-b32
description: "Store 32 bits of data from one vector input register and then 32 bits of data from a second vector input register into a data share."
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

# DS_WRITE2_B32

Store 32 bits of data from one vector input register and then 32 bits of data from a second vector input register into a data share.

## Encoding

Encoding: `ENC_DS`
Opcode: `14`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 32bit | in | no |
| DATA1 | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | DSMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Writes two 32-bit values to LDS using a single base address and two independent immediate offsets. Helps reduce instruction count when scattering data into shared memory.

## Example
```cpp
__device__ void write2_lds(uint32_t lds_offset, float v1, float v2) {
    asm volatile(
        "ds_write2_b32 %0, %1, %2 offset0:0 offset1:1" 
        : : "v"(lds_offset), "v"(__float_as_uint(v1)), "v"(__float_as_uint(v2))
    );
}
```
