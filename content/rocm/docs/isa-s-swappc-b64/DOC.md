---
name: isa-s-swappc-b64
description: "Store the address of the next instruction to a scalar register and then jump to an address specified in the scalar input."
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

# S_SWAPPC_B64

Store the address of the next instruction to a scalar register and then jump to an address specified in the scalar input.

## Encoding

Encoding: `ENC_SOP1`
Opcode: `30`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 64bit | out | no |
| SSRC0 | SREG | 64bit | in | no |
|  | PC | 64bit | out | yes |


## Flags

- IsBranch
- IsIndirectBranch

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
