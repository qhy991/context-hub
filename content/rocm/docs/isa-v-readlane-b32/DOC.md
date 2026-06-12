---
name: isa-v-readlane-b32
description: "Read the scalar value in the specified lane of the first input where the lane select is in the second input. Store the result into a scalar register."
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

# V_READLANE_B32

Read the scalar value in the specified lane of the first input where the lane select is in the second input. Store the result into a scalar register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `649`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | SREG_NOVCC | 32bit | out | no |
| SRC0 | VGPR_OR_LDS | 32bit | in | no |
| SRC1 | SSRC_LANESEL | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
