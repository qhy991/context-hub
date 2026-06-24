import os

docs = {
    "isa-v-mfma-f32-16x16x1-4b-f32": {
        "sem": "Matrix-Fused Multiply-Add for 16x16x1 blocks utilizing 4-bit precision inputs and accumulating into 32-bit floats. Accelerates extreme low-precision inference networks where parameters are highly quantized.",
        "ex": "__device__ void mfma_16x16x1_4b_f32(float& d_out, int a, int b, float c) {\n    // Intrinsic representing 4-bit MFMA operation\n    d_out = __builtin_amdgcn_mfma_f32_16x16x1_4b_f32(a, b, c, 0, 0, 0);\n}"
    }
}

for k, v in docs.items():
    p = os.path.join("/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/docs/", k, "DOC.md")
    with open(p, "a") as f:
        f.write("\n## Semantics\n" + v["sem"] + "\n\n## Example\n```cpp\n" + v["ex"] + "\n```\n")

print("Docs updated successfully. Total:", len(docs))
