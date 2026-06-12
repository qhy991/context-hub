---
name: hip-hipdeviceattribute_t
description: "Enumeration type for DeviceAttribute t."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,hip,runtime-api,device-management
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: Device Management
---

# hipDeviceAttribute_t

Enumeration type for DeviceAttribute t.

## Type

Enum. typedef enum hipDeviceAttribute_t {

## Values

`hipDeviceAttributeCudaCompatibleBegin`, `hipDeviceAttributeEccEnabled`, `hipDeviceAttributeCudaCompatibleEnd`, `hipDeviceAttributeAmdSpecificBegin`, `hipDeviceAttributeClockInstructionRate`, `hipDeviceAttributeAmdSpecificEnd`, `hipDeviceAttributeVendorSpecificBegin`

## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___device.html#gacc0acd7b9bda126c6bb3dfd6e2796d7c)
