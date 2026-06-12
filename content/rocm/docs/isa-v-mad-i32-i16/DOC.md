---
name: isa-v-mad-i32-i16
description: "Multiply two signed 16-bit integer inputs in the signed 32-bit integer domain, add a signed 32-bit integer value from a third input, and store the result as a signed 32-bit integer into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_MAD_I32_I16

Multiply two signed 16-bit integer inputs in the signed 32-bit integer domain, add a signed 32-bit integer value from a third input, and store the result as a signed 32-bit integer into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `498`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |
| SRC2 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
