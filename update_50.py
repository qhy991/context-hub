import os

docs = {
    "hip-hipMalloc": {
        "sem": "Allocates memory on the device (GPU). Under the hood, it interacts with the AMD HSA/ROCr runtime to allocate a region of global memory and map it to the GPU's virtual address space. This memory is typically unpageable and resides in the GPU's high-bandwidth VRAM.",
        "ex": "#include <hip/hip_runtime.h>\n#include <iostream>\n\nint main() {\n    float* d_A;\n    size_t bytes = 1024 * sizeof(float);\n    \n    hipError_t err = hipMalloc(&d_A, bytes);\n    if (err != hipSuccess) {\n        std::cerr << \"hipMalloc failed: \" << hipGetErrorString(err) << std::endl;\n        return -1;\n    }\n    \n    // Free memory\n    hipFree(d_A);\n    return 0;\n}"
    },
    "hip-hipfree": {
        "sem": "Frees memory previously allocated on the device via `hipMalloc`. It communicates with the ROCr memory manager to unmap and return the physical pages to the GPU memory pool. Freeing null pointers is a no-op.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid cleanup(float* d_ptr) {\n    if (d_ptr != nullptr) {\n        hipFree(d_ptr);\n    }\n}"
    },
    "hip-hipmemcpy": {
        "sem": "Copies data between host and device or device and device. It automatically infers the direction based on the pointers if unified virtual addressing is active, but performance is optimized when the correct `hipMemcpyKind` is specified. Under the hood, it may use synchronous SDMA engine transfers or host-side mapping.",
        "ex": "#include <hip/hip_runtime.h>\n#include <vector>\n\nint main() {\n    size_t N = 256;\n    size_t bytes = N * sizeof(float);\n    std::vector<float> h_A(N, 1.0f);\n    float* d_A;\n    \n    hipMalloc(&d_A, bytes);\n    // Host to Device\n    hipMemcpy(d_A, h_A.data(), bytes, hipMemcpyHostToDevice);\n    \n    // Device to Host\n    hipMemcpy(h_A.data(), d_A, bytes, hipMemcpyDeviceToHost);\n    \n    hipFree(d_A);\n    return 0;\n}"
    },
    "hip-hipmemcpyasync": {
        "sem": "Asynchronously copies data using a specific stream. It pushes a memory transfer command into the stream's command queue. For Host-to-Device or Device-to-Host transfers to be truly asynchronous, the host memory must be page-locked (pinned) using `hipHostMalloc` or `hipHostRegister`.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid async_transfer(float* d_dest, float* h_src, size_t bytes, hipStream_t stream) {\n    // Assuming h_src is pinned memory\n    hipMemcpyAsync(d_dest, h_src, bytes, hipMemcpyHostToDevice, stream);\n    // Note: Do not access h_src or d_dest until stream is synchronized\n}"
    },
    "hip-hipmemcpy2d": {
        "sem": "Copies a 2D matrix with specific pitch (stride). It performs a structured copy of elements, reading `width` bytes from each row and advancing by `spitch` on the source and `dpitch` on the destination. It is translated to specialized 2D SDMA copy commands.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid copy_2d_matrix(float* d_dest, size_t dpitch, float* h_src, size_t spitch, size_t width, size_t height) {\n    hipMemcpy2D(d_dest, dpitch, h_src, spitch, width, height, hipMemcpyHostToDevice);\n}"
    },
    "hip-hipmemcpy3d": {
        "sem": "Copies a 3D block of memory. Utilizes `hipMemcpy3DParms` to describe the 3D extent, source/destination pointers, and pitch/slice configurations. Handled by the SDMA engine via specialized 3D linear-to-linear, linear-to-tiled, or tiled-to-tiled transfers.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid copy_3d(hipPitchedPtr dest, hipPitchedPtr src, hipExtent extent) {\n    hipMemcpy3DParms params = {0};\n    params.srcPtr = src;\n    params.dstPtr = dest;\n    params.extent = extent;\n    params.kind = hipMemcpyDeviceToDevice;\n    hipMemcpy3D(&params);\n}"
    },
    "hip-hipmemcpydtod": {
        "sem": "Specifically performs a Device-to-Device memory copy. It skips the heuristic pointer-location checks of `hipMemcpy`, directly enqueuing an SDMA (System DMA) or compute-shader based local VRAM copy command.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid clone_buffer(float* d_dest, const float* d_src, size_t bytes) {\n    hipMemcpyDtoD(d_dest, d_src, bytes);\n}"
    },
    "hip-hipmemcpydtoh": {
        "sem": "Specifically performs a Device-to-Host memory copy. Data is moved from GPU VRAM to CPU system memory over PCIe or xGMI.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid fetch_results(float* h_dest, const float* d_src, size_t bytes) {\n    hipMemcpyDtoH(h_dest, d_src, bytes);\n}"
    },
    "hip-hipmemcpyhtod": {
        "sem": "Specifically performs a Host-to-Device memory copy. Data is moved from CPU system memory to GPU VRAM.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid upload_weights(float* d_dest, const float* h_src, size_t bytes) {\n    hipMemcpyHtoD(d_dest, h_src, bytes);\n}"
    },
    "hip-hipstreamcreate": {
        "sem": "Creates an asynchronous execution stream. A stream corresponds to a hardware or software command queue in the ROCr runtime. Commands placed in the same stream execute strictly in order.",
        "ex": "#include <hip/hip_runtime.h>\n\nint main() {\n    hipStream_t stream;\n    hipStreamCreate(&stream);\n    \n    // ... launch kernels on stream ...\n    \n    hipStreamDestroy(stream);\n    return 0;\n}"
    },
    "hip-hipstreamdestroy": {
        "sem": "Destroys an asynchronous execution stream, freeing the associated ROCr command queue resources. It blocks until all previously enqueued work in the stream completes.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid cleanup_stream(hipStream_t stream) {\n    hipStreamDestroy(stream);\n}"
    },
    "hip-hipstreamsynchronize": {
        "sem": "Blocks the host CPU thread until all commands enqueued in the specified stream have completed execution on the device. Underneath, it polls the completion signal or uses HSA sleep wait functions.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid wait_for_stream(hipStream_t stream) {\n    hipStreamSynchronize(stream);\n}"
    },
    "hip-hipstreamwaitvalue32": {
        "sem": "Instructs the stream to wait on a specific 32-bit value in memory before continuing. This is a highly efficient way to synchronize streams without host intervention, leveraging hardware-level memory polling.",
        "ex": "#include <hip/hip_runtime.h>\n#include <hip/hip_ext.h>\n\nvoid wait_on_flag(hipStream_t stream, uint32_t* d_flag, uint32_t wait_val) {\n    hipStreamWaitValue32(stream, d_flag, wait_val, hipStreamWaitValueEq);\n}"
    },
    "hip-hipstreamwritevalue32": {
        "sem": "Enqueues a command in the stream to write a 32-bit value to a specified memory location. Often used in tandem with `hipStreamWaitValue32` for low-latency device-side stream synchronization.",
        "ex": "#include <hip/hip_runtime.h>\n#include <hip/hip_ext.h>\n\nvoid signal_completion(hipStream_t stream, uint32_t* d_flag, uint32_t signal_val) {\n    hipStreamWriteValue32(stream, d_flag, signal_val, 0);\n}"
    },
    "hip-hipeventcreate": {
        "sem": "Creates a HIP event object. An event is used for timing or synchronization. It allocates an HSA signal (or analogous structure) that can track a specific point in a stream's execution.",
        "ex": "#include <hip/hip_runtime.h>\n\nint main() {\n    hipEvent_t event;\n    hipEventCreate(&event);\n    hipEventDestroy(event);\n    return 0;\n}"
    },
    "hip-hipeventdestroy": {
        "sem": "Destroys a HIP event object, releasing the underlying signaling resources back to the runtime.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid cleanup_event(hipEvent_t event) {\n    hipEventDestroy(event);\n}"
    },
    "hip-hipeventrecord": {
        "sem": "Records an event in a stream. The event will be triggered (signaled) when all preceding commands in the stream have finished executing. Useful for stream synchronization or latency measurement.",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid mark_stream(hipStream_t stream, hipEvent_t event) {\n    hipEventRecord(event, stream);\n}"
    },
    "hip-hipeventsynchronize": {
        "sem": "Blocks the host CPU thread until the specified event has been recorded (i.e., until the command queue passes the event marker).",
        "ex": "#include <hip/hip_runtime.h>\n\nvoid wait_for_event(hipEvent_t event) {\n    hipEventSynchronize(event);\n}"
    },
    "hip-hipeventelapsedtime": {
        "sem": "Calculates the execution time (in milliseconds) elapsed between two recorded events. Resolves the difference between the GPU hardware timestamps captured when the start and stop events were signaled.",
        "ex": "#include <hip/hip_runtime.h>\n#include <iostream>\n\nvoid measure_time(hipEvent_t start, hipEvent_t stop) {\n    float ms = 0.0f;\n    hipEventElapsedTime(&ms, start, stop);\n    std::cout << \"Kernel took \" << ms << \" ms\" << std::endl;\n}"
    },
    "hip-hiplaunchkernel": {
        "sem": "Enqueues a kernel for execution on the GPU. Configures the hardware packet (e.g., AQL packet in HSA) containing the grid/block dimensions, shared memory size, and arguments, dispatching it to the command processor (CP).",
        "ex": "#include <hip/hip_runtime.h>\n\n__global__ void my_kernel(float* a) {\n    int idx = threadIdx.x + blockIdx.x * blockDim.x;\n    a[idx] *= 2.0f;\n}\n\nvoid run_kernel(float* d_a) {\n    void* args[] = { &d_a };\n    hipLaunchKernel((const void*)my_kernel, dim3(10), dim3(256), args, 0, nullptr);\n}"
    },
    "hip-hiplaunchkernelexc": {
        "sem": "Similar to `hipLaunchKernel`, but often allows for additional runtime configuration and extended features. Used internally to serialize and dispatch the kernel with specific execution parameters.",
        "ex": "#include <hip/hip_runtime.h>\n\n// Typically accessed via the triple-chevron launch syntax in HIP\n// my_kernel<<<dim3(10), dim3(256), 0, stream>>>(d_a);"
    },
    "isa-ds-read-b32": {
        "sem": "Reads a 32-bit (dword) value from Local Data Share (LDS). Uses an address specified in a VGPR and an optional immediate offset. The LDS is the shared memory on AMD GPUs, characterized by high bandwidth and low latency, mapped into a single compute unit.",
        "ex": "// Using inline assembly to perform LDS read\n__device__ float read_lds(uint32_t lds_offset) {\n    float val;\n    asm volatile(\n        \"ds_read_b32 %0, %1 offset:0\" \n        : \"=v\"(val) : \"v\"(lds_offset)\n    );\n    return val;\n}"
    },
    "isa-ds-read-b128": {
        "sem": "Reads 128 bits (4 dwords) from Local Data Share (LDS). Extremely useful for vectorized memory loads from shared memory in matrix multiplication and AI kernels to maximize bandwidth.",
        "ex": "__device__ float4 read_lds_128(uint32_t lds_offset) {\n    float4 val;\n    asm volatile(\n        \"ds_read_b128 %0, %1 offset:0\" \n        : \"=v\"(val) : \"v\"(lds_offset)\n    );\n    return val;\n}"
    },
    "isa-ds-write-b32": {
        "sem": "Writes a 32-bit (dword) value to Local Data Share (LDS). Often used to stage global memory data into shared memory for cooperative thread block processing.",
        "ex": "__device__ void write_lds(uint32_t lds_offset, float val) {\n    asm volatile(\n        \"ds_write_b32 %0, %1 offset:0\" \n        : : \"v\"(lds_offset), \"v\"(val)\n    );\n}"
    },
    "isa-ds-write-b128": {
        "sem": "Writes 128 bits (4 dwords) to Local Data Share (LDS). Used for high-throughput vectorized shared memory stores.",
        "ex": "__device__ void write_lds_128(uint32_t lds_offset, float4 val) {\n    asm volatile(\n        \"ds_write_b128 %0, %1 offset:0\" \n        : : \"v\"(lds_offset), \"v\"(val)\n    );\n}"
    },
    "isa-ds-read2-b32": {
        "sem": "Reads two 32-bit values from LDS using a single base address and two independent immediate offsets. Optimizes instruction cache usage and memory subsystem scheduling.",
        "ex": "__device__ void read2_lds(uint32_t lds_offset, float& v1, float& v2) {\n    uint2 res;\n    asm volatile(\n        \"ds_read2_b32 %0, %1 offset0:0 offset1:1\" \n        : \"=v\"(res) : \"v\"(lds_offset)\n    );\n    v1 = __uint_as_float(res.x);\n    v2 = __uint_as_float(res.y);\n}"
    },
    "isa-ds-write2-b32": {
        "sem": "Writes two 32-bit values to LDS using a single base address and two independent immediate offsets. Helps reduce instruction count when scattering data into shared memory.",
        "ex": "__device__ void write2_lds(uint32_t lds_offset, float v1, float v2) {\n    asm volatile(\n        \"ds_write2_b32 %0, %1, %2 offset0:0 offset1:1\" \n        : : \"v\"(lds_offset), \"v\"(__float_as_uint(v1)), \"v\"(__float_as_uint(v2))\n    );\n}"
    },
    "isa-ds-add-u32": {
        "sem": "Atomically adds an unsigned 32-bit integer to a value in LDS. Ensures serialization of operations across threads in a workgroup attempting to update the same LDS location.",
        "ex": "__device__ void atomic_add_lds(uint32_t lds_offset, uint32_t inc) {\n    asm volatile(\n        \"ds_add_u32 %0, %1 offset:0\" \n        : : \"v\"(lds_offset), \"v\"(inc)\n    );\n}"
    },
    "isa-ds-bpermute-b32": {
        "sem": "Performs a byte-wise cross-lane permute within a wavefront. Allows a lane to read a 32-bit value from any other lane in the same wave based on a byte offset, heavily used in butterfly reductions.",
        "ex": "__device__ int bpermute(int index, int val) {\n    int result;\n    asm volatile(\n        \"ds_bpermute_b32 %0, %1, %2\" \n        : \"=v\"(result) : \"v\"(index << 2), \"v\"(val)\n    );\n    return result;\n}"
    },
    "isa-v-mfma-f32-16x16x16f16": {
        "sem": "Matrix-Fused Multiply-Add for 16x16x16 half-precision (fp16) tiles, accumulating into 32-bit floats. Central to CDNA matrix cores, executing a massive block of MAC operations efficiently.",
        "ex": "__device__ void mfma_16x16x16_fp16(float32_t& d_out, half16_t a, half16_t b, float32_t c) {\n    // Pseudocode abstraction of __builtin_amdgcn_mfma_f32_16x16x16f16\n    d_out = __builtin_amdgcn_mfma_f32_16x16x16f16(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-32x32x8f16": {
        "sem": "Matrix-Fused Multiply-Add for 32x32x8 half-precision tiles, accumulating into 32-bit floats. Designed for large gemm shapes to maximize throughput and register reuse.",
        "ex": "__device__ void mfma_32x32x8_fp16(float32_t& d_out, half8_t a, half8_t b, float32_t c) {\n    d_out = __builtin_amdgcn_mfma_f32_32x32x8f16(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-16x16x4f32": {
        "sem": "Matrix-Fused Multiply-Add for 16x16x4 single-precision (fp32) tiles, accumulating into fp32. Uses matrix cores to accelerate full precision matrix multiplication.",
        "ex": "__device__ void mfma_16x16x4_fp32(float32_t& d_out, float4_t a, float4_t b, float32_t c) {\n    d_out = __builtin_amdgcn_mfma_f32_16x16x4f32(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-32x32x2f32": {
        "sem": "Matrix-Fused Multiply-Add for 32x32x2 single-precision tiles, accumulating into fp32. Reduces memory bandwidth pressure for operations bounded by throughput at fp32 precision.",
        "ex": "__device__ void mfma_32x32x2_fp32(float32_t& d_out, float2_t a, float2_t b, float32_t c) {\n    d_out = __builtin_amdgcn_mfma_f32_32x32x2f32(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-16x16x16bf16-1k": {
        "sem": "Matrix-Fused Multiply-Add for 16x16x16 bfloat16 tiles, accumulating into fp32. Supports deep neural network training by providing higher dynamic range natively.",
        "ex": "__device__ void mfma_16x16x16_bf16(float32_t& d_out, bfloat16_16_t a, bfloat16_16_t b, float32_t c) {\n    d_out = __builtin_amdgcn_mfma_f32_16x16x16bf16_1k(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-i32-16x16x16i8": {
        "sem": "Matrix-Fused Multiply-Add for 16x16x16 INT8 tiles, accumulating into 32-bit integers. Essential for quantized integer inference architectures and low-precision AI tasks.",
        "ex": "__device__ void mfma_16x16x16_int8(int32_t& d_out, int8_16_t a, int8_16_t b, int32_t c) {\n    d_out = __builtin_amdgcn_mfma_i32_16x16x16i8(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-16x16x128-f8f6f4": {
        "sem": "Matrix-Fused Multiply-Add using emerging FP8 formats. Processes an exceptionally deep 128-element dimension per step to heavily amortize register loading costs, accelerating transformer inference.",
        "ex": "// Conceptual usage for FP8 matrix operations\n__device__ void mfma_16x16x128_fp8(float& d_out, uint32_t a[4], uint32_t b[4], float c) {\n    d_out = __builtin_amdgcn_mfma_f32_16x16x128_f8f6f4(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-mfma-f32-32x32x64-f8f6f4": {
        "sem": "Matrix-Fused Multiply-Add using FP8 for large 32x32 matrix tiles with an inner dimension of 64. Drastically increases computational density on CDNA3/4 architectures.",
        "ex": "// Conceptual usage for FP8 32x32x64\n__device__ void mfma_32x32x64_fp8(float& d_out, uint32_t a[2], uint32_t b[2], float c) {\n    d_out = __builtin_amdgcn_mfma_f32_32x32x64_f8f6f4(a, b, c, 0, 0, 0);\n}"
    },
    "isa-v-fmac-f32": {
        "sem": "Vector Fused Multiply-Add (in-place accumulation). Computes `vd = vd + (vs1 * vs2)` with a single rounding step. Uses fewer registers than v_fma_f32 as the destination is also the addend.",
        "ex": "__device__ void v_fmac(float& acc, float a, float b) {\n    asm volatile(\n        \"v_fmac_f32 %0, %1, %2\" \n        : \"+v\"(acc) : \"v\"(a), \"v\"(b)\n    );\n}"
    },
    "isa-v-mac-f32": {
        "sem": "Vector Multiply-Add. Conceptually similar to fmac but does not guarantee fused rounding (may round the multiplication before addition depending on legacy hardware behavior, though often synonymous in modern ISAs).",
        "ex": "__device__ void v_mac(float& acc, float a, float b) {\n    asm volatile(\n        \"v_mac_f32 %0, %1, %2\" \n        : \"+v\"(acc) : \"v\"(a), \"v\"(b)\n    );\n}"
    },
    "isa-v-add-f32": {
        "sem": "Vector floating-point addition. Adds two 32-bit floating-point registers. Supports input modifiers like negation and absolute value directly encoded in the instruction.",
        "ex": "__device__ float v_add(float a, float b) {\n    float res;\n    asm volatile(\"v_add_f32 %0, %1, %2\" : \"=v\"(res) : \"v\"(a), \"v\"(b));\n    return res;\n}"
    },
    "isa-v-mul-f32": {
        "sem": "Vector floating-point multiplication. Multiplies two 32-bit floating-point registers. Optimized for high throughput in the shader ALUs.",
        "ex": "__device__ float v_mul(float a, float b) {\n    float res;\n    asm volatile(\"v_mul_f32 %0, %1, %2\" : \"=v\"(res) : \"v\"(a), \"v\"(b));\n    return res;\n}"
    },
    "isa-v-mov-b32": {
        "sem": "Moves a 32-bit value between vector registers, or loads an immediate/scalar value into a vector register. Extremely common for register shuffling and initialization.",
        "ex": "__device__ float v_mov(float a) {\n    float res;\n    asm volatile(\"v_mov_b32 %0, %1\" : \"=v\"(res) : \"v\"(a));\n    return res;\n}"
    },
    "isa-v-cmp-eq-f32": {
        "sem": "Vector compare equal. Compares two 32-bit floating-point registers. It outputs a boolean mask to the VCC (Vector Condition Code) register, representing the per-lane comparison results.",
        "ex": "__device__ bool v_cmp_eq(float a, float b) {\n    // High-level abstraction\n    return a == b;\n}"
    },
    "isa-v-dot2-f32-f16": {
        "sem": "Computes the dot product of two half-precision (f16) pairs and accumulates into a 32-bit float. Ideal for dual-issue ML operations on packed f16 vectors.",
        "ex": "__device__ float v_dot2_f16(float2 a, float2 b, float acc) {\n    // Abstraction of v_dot2_f32_f16\n    return __builtin_amdgcn_fdot2(a, b, acc, false);\n}"
    },
    "isa-v-dot2c-f32-f16": {
        "sem": "Computes a complex dot product of two half-precision pairs or uses a specific clamped accumulation, depending on hardware generation. Further optimizes specialized activation/accumulation paths.",
        "ex": "__device__ float v_dot2c_f16(float2 a, float2 b, float acc) {\n    // Hardware-specific complex dot product intrinsic\n    return __builtin_amdgcn_fdot2(a, b, acc, true);\n}"
    },
    "isa-v-dot4-i32-i8": {
        "sem": "Computes the dot product of four 8-bit integers (packed in a 32-bit register) and accumulates the result into a 32-bit integer register. Essential for INT8 AI inference.",
        "ex": "__device__ int v_dot4_i8(int a, int b, int acc) {\n    return __builtin_amdgcn_sdot4(a, b, acc, false);\n}"
    },
    "isa-v-add-f16": {
        "sem": "Vector floating-point addition for 16-bit half-precision numbers. Often executed at 2x rate compared to FP32 if packed math (PK) is utilized, or acts directly on low 16-bits of the register.",
        "ex": "__device__ _Float16 v_add_f16(_Float16 a, _Float16 b) {\n    return a + b;\n}"
    },
    "isa-v-mul-f16": {
        "sem": "Vector floating-point multiplication for 16-bit half-precision numbers. Provides high throughput for FP16 math directly within the standard ALU pipeline.",
        "ex": "__device__ _Float16 v_mul_f16(_Float16 a, _Float16 b) {\n    return a * b;\n}"
    },
    "isa-v-max-f32": {
        "sem": "Vector maximum operation. Compares two 32-bit floating point registers lane-by-lane and writes the maximum into the destination register. Often mapped to `fmaxf` in C++.",
        "ex": "__device__ float v_max(float a, float b) {\n    return fmaxf(a, b);\n}"
    }
}

for k, v in docs.items():
    p = os.path.join("/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/docs/", k, "DOC.md")
    with open(p, "a") as f:
        f.write("\n## Semantics\n" + v["sem"] + "\n\n## Example\n```cpp\n" + v["ex"] + "\n```\n")

print("Docs updated successfully. Total:", len(docs))
