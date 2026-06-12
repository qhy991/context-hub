---
name: isa-s-cselect-b64
description: "Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_CSELECT_B64

Select the first input if SCC is true otherwise select the second input, then store the selected input into a scalar register.

## Encoding

Encoding: `ENC_SOP2`
Opcode: `11`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 64bit | out | no |
| SSRC0 | SSRC | 64bit | in | no |
| SSRC1 | SSRC | 64bit | in | no |
|  | SSRC_SPECIAL_SCC | 1bit | in | yes |
| LITERAL | SSRC | 64bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
