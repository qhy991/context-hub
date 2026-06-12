---
name: isa-v-ffbl-b32
description: "Count the number of trailing \"0\" bits before the first \"1\" in a vector input and store the result into a vector register. Store -1 if there are no \"1\" bits in the input."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_FFBL_B32

Count the number of trailing "0" bits before the first "1" in a vector input and store the result into a vector register. Store -1 if there are no "1" bits in the input.

## Encoding

Encoding: `ENC_VOP1`
Opcode: `46`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |
| VSRC0 | VGPR | 32bit | in | no |
| VSRC0 | SRC_SIMPLE | 32bit | in | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
