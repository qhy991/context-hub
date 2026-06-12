---
name: isa-v-permlane16-swap-b32
description: "Swap data between two vector registers. Odd rows of the first operand are swapped with even rows of the second operand (one row is 16 lanes)."
metadata:
  languages: hip
  architectures: cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP1
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_PERMLANE16_SWAP_B32

Swap data between two vector registers. Odd rows of the first operand are swapped with even rows of the second operand (one row is 16 lanes).

## Encoding

Encoding: `ENC_VOP1`
Opcode: `89`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_VGPR | 32bit | out | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
