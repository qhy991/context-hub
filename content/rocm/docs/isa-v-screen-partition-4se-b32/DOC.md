---
name: isa-v-screen-partition-4se-b32
description: "4SE version of LUT instruction for screen partitioning/filtering. This opcode is intended to help accelerate screen partitioning in the 4SE case only. 2SE and 1SE cases use normal ALU instructions."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_SCREEN_PARTITION_4SE_B32

4SE version of LUT instruction for screen partitioning/filtering. This opcode is intended to help accelerate screen partitioning in the 4SE case only. 2SE and 1SE cases use normal ALU instructions.

## Encoding

Encoding: `ENC_VOP1`
Opcode: `55`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |
| VSRC0 | VGPR | 32bit | in | no |
| VSRC0 | SRC_SIMPLE | 32bit | in | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
