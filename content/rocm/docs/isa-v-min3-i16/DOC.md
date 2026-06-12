---
name: isa-v-min3-i16
description: "Select the minimum of three signed 16-bit integer inputs and store the selected value into a vector register."
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

# V_MIN3_I16

Select the minimum of three signed 16-bit integer inputs and store the selected value into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `501`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |
| SRC2 | SRC_SIMPLE | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
