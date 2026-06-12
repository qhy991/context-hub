---
name: isa-v-accvgpr-write
description: "Move 32 bits of data from an architectural vector register into an accumulator vector register."
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

# V_ACCVGPR_WRITE

Move 32 bits of data from an architectural vector register into an accumulator vector register.

## Encoding

Encoding: `ENC_VOP3P`
Opcode: `89`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | ACCVGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
