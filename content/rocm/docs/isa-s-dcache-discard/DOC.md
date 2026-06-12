---
name: isa-s-dcache-discard
description: "Discard one dirty scalar data L0 cache line. A cache line is 64 bytes."
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
  func_group: SMEM
  arch_name: AMD CDNA 4
---

# S_DCACHE_DISCARD

Discard one dirty scalar data L0 cache line. A cache line is 64 bytes.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `40`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SBASE | SREG | 64bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
