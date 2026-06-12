---
name: isa-v-subb-co-u32
description: "Subtract the second unsigned 32-bit integer input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register."
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

# V_SUBB_CO_U32

Subtract the second unsigned 32-bit integer input from the first input, subtract a bit from the carry-in mask, store the result into a vector register and store the carry-out mask into a scalar register.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `29`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
|  | VCC | 64bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |
| VSRC0 | VGPR | 32bit | in | no |
| SDST | SREG | 64bit | out | no |
| VSRC0 | SRC_SIMPLE | 32bit | in | no |
| VSRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC2 | SREG | 64bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
