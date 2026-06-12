---
name: isa-v-fmamk-f32
description: "Multiply a single-precision float input with a literal constant and add a second single-precision float input using fused multiply add, and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna3,cdna4
  versions: 'CDNA4+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_FMAMK_F32

Multiply a single-precision float input with a literal constant and add a second single-precision float input using fused multiply add, and store the result into a vector register.

## Encoding

Encoding: `VOP2_INST_LITERAL`
Opcode: `23`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| LITERAL | SIMM32 | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
