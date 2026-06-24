---
name: isa-v-cmp-eq-f32
description: "Set the per-lane condition code to 1 iff the first input is equal to the second input. Store the result into VCC or a scalar register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,flow,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: flow
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CMP_EQ_F32

Set the per-lane condition code to 1 iff the first input is equal to the second input. Store the result into VCC or a scalar register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `66`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | SREG | 64bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |
|  | VCC | 64bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |
| SDST | SREG | 64bit | out | no |
| VSRC0 | SRC_SIMPLE | 32bit | in | no |
| VSRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Vector compare equal. Compares two 32-bit floating-point registers. It outputs a boolean mask to the VCC (Vector Condition Code) register, representing the per-lane comparison results.

## Example
```cpp
__device__ bool v_cmp_eq(float a, float b) {
    // High-level abstraction
    return a == b;
}
```
