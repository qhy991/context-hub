---
name: isa-s-sext-i32-i8
description: "Sign extend a signed 8 bit scalar input to 32 bits and store the result into a scalar register."
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

# S_SEXT_I32_I8

Sign extend a signed 8 bit scalar input to 32 bits and store the result into a scalar register.

## Encoding

Encoding: `ENC_SOP1`
Opcode: `22`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 32bit | out | no |
| SSRC0 | SSRC | 8bit | in | no |
| LITERAL | SSRC | 8bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
