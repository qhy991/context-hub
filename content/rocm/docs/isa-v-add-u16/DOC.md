---
name: isa-v-add-u16
description: "Add two unsigned 16-bit integer inputs and store the result into a vector register. No carry-in or carry-out support."
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

# V_ADD_U16

Add two unsigned 16-bit integer inputs and store the result into a vector register. No carry-in or carry-out support.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `38`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC | 16bit | in | no |
| VSRC1 | VGPR | 16bit | in | no |
| LITERAL | SRC | 16bit | in | no |
| VSRC0 | VGPR | 16bit | in | no |
| VSRC0 | SRC_SIMPLE | 16bit | in | no |
| VSRC1 | SRC_SIMPLE | 16bit | in | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
