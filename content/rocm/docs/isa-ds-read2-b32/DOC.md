---
name: isa-ds-read2-b32
description: "Load 32 bits of data from one location in a data share and then 32 bits of data from a second location in a data share and store the results into a 64-bit vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_READ2_B32

Load 32 bits of data from one location in a data share and then 32 bits of data from a second location in a data share and store the results into a 64-bit vector register.

## Encoding

Encoding: `ENC_DS`
Opcode: `55`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Reads two 32-bit values from LDS using a single base address and two independent immediate offsets. Optimizes instruction cache usage and memory subsystem scheduling.

## Example
```cpp
__device__ void read2_lds(uint32_t lds_offset, float& v1, float& v2) {
    uint2 res;
    asm volatile(
        "ds_read2_b32 %0, %1 offset0:0 offset1:1" 
        : "=v"(res) : "v"(lds_offset)
    );
    v1 = __uint_as_float(res.x);
    v2 = __uint_as_float(res.y);
}
```
