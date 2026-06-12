---
name: isa-s-barrier
description: "Synchronize waves within a threadgroup."
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
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_BARRIER

Synchronize waves within a threadgroup.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `10`



## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
