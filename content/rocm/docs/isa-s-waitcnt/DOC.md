---
name: isa-s-waitcnt
description: "Wait for the counts of outstanding local data share, vector memory and export instructions to be at or below the specified levels."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scheduler,synchronization
  isa_category: synchronization
  instruction_type: SOP
  hw_unit: scheduler
  func_group: WAVE_CONTROL
  arch_name: AMD CDNA 4
---

# S_WAITCNT

Wait for the counts of outstanding local data share, vector memory and export instructions to be at or below the specified levels.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `12`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SIMM16 | WAITCNT | 16bit | in | no |


## Flags

- IsImmediatelyExecuted

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
