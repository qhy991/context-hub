---
name: isa-v-cvt-u32-f64
description: "Convert from a double-precision float input to an unsigned 32-bit integer value and store the result into a vector register."
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

# V_CVT_U32_F64

Convert from a double-precision float input to an unsigned 32-bit integer value and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP1`
Opcode: `21`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC | 64bit | in | no |
| LITERAL | SRC | 64bit | in | no |
| VSRC0 | VGPR | 64bit | in | no |
| SRC0 | SRC_NOLIT | 64bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
