---
name: isa-v-mad-f32
description: "Multiply two single-precision float inputs and add a third input, and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 2
---

# V_MAD_F32

Multiply two single-precision float inputs and add a third input, and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `449`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC2 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
