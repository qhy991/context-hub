---
name: isa-v-ashrrev-i32
description: "Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register."
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

# V_ASHRREV_I32

Given a shift count in the first vector input, calculate the arithmetic shift right (preserving sign bit) of the second vector input and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `17`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLDS | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| LITERAL | SRC_NOLDS | 32bit | in | no |
| VSRC0 | VGPR | 32bit | in | no |
| VSRC0 | SRC_NOLDS | 32bit | in | no |
| VSRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC0 | SRC_SIMPLE | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
