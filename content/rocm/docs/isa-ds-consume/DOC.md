---
name: isa-ds-consume
description: "Subtract (count_bits(exec_mask)) from the value stored in DS memory at (M0.base + instr_offset) if GDS, or at instr_offset if LDS. Return the pre-operation value to VGPRs."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_CONSUME

Subtract (count_bits(exec_mask)) from the value stored in DS memory at (M0.base + instr_offset) if GDS, or at instr_offset if LDS. Return the pre-operation value to VGPRs.

## Encoding

Encoding: `ENC_DS`
Opcode: `189`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
|  | DSMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
