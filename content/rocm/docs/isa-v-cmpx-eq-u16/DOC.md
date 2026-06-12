---
name: isa-v-cmpx-eq-u16
description: "Set the per-lane condition code to 1 iff the first input is equal to the second input. Store the result into the EXEC mask and to VCC or a scalar register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,flow,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: flow
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CMPX_EQ_U16

Set the per-lane condition code to 1 iff the first input is equal to the second input. Store the result into the EXEC mask and to VCC or a scalar register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `186`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | SDST | 64bit | out | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |
|  | SDST_EXEC | 64bit | out | yes |
|  | VCC | 64bit | out | no |
| SRC0 | SRC | 16bit | in | no |
| VSRC1 | VGPR | 16bit | in | no |
| LITERAL | SRC | 16bit | in | no |
| SDST | SREG | 64bit | out | no |
| VSRC0 | SRC_SIMPLE | 16bit | in | no |
| VSRC1 | SRC_SIMPLE | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
