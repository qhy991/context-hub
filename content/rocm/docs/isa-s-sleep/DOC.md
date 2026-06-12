---
name: isa-s-sleep
description: "Cause a wave to sleep for up to ~8000 clocks."
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

# S_SLEEP

Cause a wave to sleep for up to ~8000 clocks.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `14`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SIMM16 | SIMM16 | 16bit | in | no |


## Flags

- IsImmediatelyExecuted

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
