---
name: isa-s-set-gpr-idx-on
description: "Enable GPR indexing mode."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_SET_GPR_IDX_ON

Enable GPR indexing mode.

## Encoding

Encoding: `ENC_SOPC`
Opcode: `17`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SSRC0 | SSRC | 32bit | in | no |
| SSRC1 | SIMM4 | 32bit | in | no |
|  | SDST_M0 | 32bit | out | yes |
| LITERAL | SSRC | 32bit | in | no |
| LITERAL | SIMM4 | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
