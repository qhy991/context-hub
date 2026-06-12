---
name: isa-s-setvskip
description: "Enables or disables VSKIP mode."
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
  func_group: WAVE_CONTROL
  arch_name: AMD CDNA 4
---

# S_SETVSKIP

Enables or disables VSKIP mode.

## Encoding

Encoding: `ENC_SOPC`
Opcode: `16`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SSRC0 | SSRC | 32bit | in | no |
| SSRC1 | SSRC | 32bit | in | no |
| LITERAL | SSRC | 32bit | in | no |


## Flags

- IsImmediatelyExecuted

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
