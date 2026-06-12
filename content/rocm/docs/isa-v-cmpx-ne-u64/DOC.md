---
name: isa-v-cmpx-ne-u64
description: "Set the per-lane condition code to 1 iff the first input is not equal to the second input. Store the result into the EXEC mask and to VCC or a scalar register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,flow,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: flow
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CMPX_NE_U64

Set the per-lane condition code to 1 iff the first input is not equal to the second input. Store the result into the EXEC mask and to VCC or a scalar register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `253`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | SDST | 64bit | out | no |
| SRC0 | SRC_NOLIT | 64bit | in | no |
| SRC1 | SRC_SIMPLE | 64bit | in | no |
|  | SDST_EXEC | 64bit | out | yes |
|  | VCC | 64bit | out | no |
| SRC0 | SRC | 64bit | in | no |
| VSRC1 | VGPR | 64bit | in | no |
| LITERAL | SRC | 64bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
