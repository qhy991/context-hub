---
name: isa-s-atomic-smax-x2
description: "Select the maximum of two signed 64-bit integer inputs, given two values stored in the data register and a location in the scalar memory. Update the scalar memory with the selected value."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow,atomic
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SMEM
  arch_name: AMD CDNA 4
---

# S_ATOMIC_SMAX_X2

Select the maximum of two signed 64-bit integer inputs, given two values stored in the data register and a location in the scalar memory. Update the scalar memory with the selected value.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `166`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDATA | SREG | 64bit | out | no |
| SBASE | SREG | 64bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
