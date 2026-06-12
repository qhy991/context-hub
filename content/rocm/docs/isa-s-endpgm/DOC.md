---
name: isa-s-endpgm
description: "End of program; terminate wavefront."
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
  func_group: MESSAGE
  arch_name: AMD CDNA 4
---

# S_ENDPGM

End of program; terminate wavefront.

## Encoding

Encoding: `ENC_SOPP`
Opcode: `1`



## Flags

- IsProgramTerminator

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
