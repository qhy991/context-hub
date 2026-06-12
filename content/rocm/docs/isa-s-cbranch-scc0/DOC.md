---
name: isa-s-cbranch-scc0
description: "If SCC is 0 then jump to a constant offset relative to the current PC."
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

# S_CBRANCH_SCC0

If SCC is 0 then jump to a constant offset relative to the current PC.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `4`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SIMM16 | LABEL | 16bit | in | no |
|  | SSRC_SPECIAL_SCC | 1bit | in | yes |


## Flags

- IsBranch
- IsConditionalBranch

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
