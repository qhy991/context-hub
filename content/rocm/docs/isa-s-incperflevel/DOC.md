---
name: isa-s-incperflevel
description: "Increment performance counter specified in SIMM16[3:0] by 1."
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

# S_INCPERFLEVEL

Increment performance counter specified in SIMM16[3:0] by 1.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `20`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SIMM16 | SIMM16 | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
