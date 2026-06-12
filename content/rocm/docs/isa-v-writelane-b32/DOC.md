---
name: isa-v-writelane-b32
description: "Write the scalar value in the first input into the specified lane of a vector register where the lane select is in the second input."
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

# V_WRITELANE_B32

Write the scalar value in the first input into the specified lane of a vector register where the lane select is in the second input.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `650`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SSRC_NOLIT | 32bit | in | no |
| SRC1 | SSRC_LANESEL | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
