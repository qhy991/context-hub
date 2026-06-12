---
name: isa-v-mbcnt-lo-u32-b32
description: "For each lane 0 <= N < 32, examine the N least significant bits of the first input and count how many of those bits are \"1\". For each lane 32 <= N < 64, all \"1\" bits in the first input are counted. Add this count to the value in the second input and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_MBCNT_LO_U32_B32

For each lane 0 <= N < 32, examine the N least significant bits of the first input and count how many of those bits are "1". For each lane 32 <= N < 64, all "1" bits in the first input are counted. Add this count to the value in the second input and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `652`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
