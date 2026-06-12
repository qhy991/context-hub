---
name: isa-v-accvgpr-mov-b32
description: "Move data from one accumulator register to another accumulator register."
metadata:
  languages: hip
  architectures: cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 3
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_ACCVGPR_MOV_B32

Move data from one accumulator register to another accumulator register.

## Encoding

Encoding: `ENC_VOP1`
Opcode: `82`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | ACCVGPR | 32bit | out | no |
| SRC0 | SRC_ACCVGPR | 32bit | in | no |
| LITERAL | SRC_ACCVGPR | 32bit | in | no |
| VSRC0 | SRC_ACCVGPR | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
