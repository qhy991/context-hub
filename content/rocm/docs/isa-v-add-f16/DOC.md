---
name: isa-v-add-f16
description: "Add two floating point inputs and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute,low-precision
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_ADD_F16

Add two floating point inputs and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `31`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC | 16bit | in | no |
| VSRC1 | VGPR | 16bit | in | no |
| LITERAL | SRC | 16bit | in | no |
| VSRC0 | VGPR | 16bit | in | no |
| VSRC0 | SRC_SIMPLE | 16bit | in | no |
| VSRC1 | SRC_SIMPLE | 16bit | in | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Vector floating-point addition for 16-bit half-precision numbers. Often executed at 2x rate compared to FP32 if packed math (PK) is utilized, or acts directly on low 16-bits of the register.

## Example
```cpp
__device__ _Float16 v_add_f16(_Float16 a, _Float16 b) {
    return a + b;
}
```
