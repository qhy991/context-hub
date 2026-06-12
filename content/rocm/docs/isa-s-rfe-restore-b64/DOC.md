---
name: isa-s-rfe-restore-b64
description: "Return from exception handler and continue. This instruction may only be used within a trap handler."
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
  func_group: TRAP
  arch_name: AMD CDNA 4
---

# S_RFE_RESTORE_B64

Return from exception handler and continue. This instruction may only be used within a trap handler.

## Encoding

Encoding: `ENC_SOP2`
Opcode: `43`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SSRC0 | SSRC | 64bit | in | no |
| SSRC1 | SSRC | 32bit | in | no |
|  | PC | 64bit | out | yes |


## Flags

- IsBranch
- IsIndirectBranch

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
