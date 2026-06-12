---
name: isa-s-set-valu-coexec-mode
description: "Set the vector ALU co-execution mode to the value encoded in SIMM16[1:0] for the next VALU instruction. The co-execution mode is cleared to zero after the next VALU instruction is issued."
metadata:
  languages: hip
  architectures: cdna3,cdna4
  versions: 'CDNA4+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_SET_VALU_COEXEC_MODE

Set the vector ALU co-execution mode to the value encoded in SIMM16[1:0] for the next VALU instruction. The co-execution mode is cleared to zero after the next VALU instruction is issued.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `31`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SIMM16 | SIMM16 | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
