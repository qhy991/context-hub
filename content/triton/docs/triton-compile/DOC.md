---
name: triton-compile
description: triton.compile — compile a Triton kernel programmatically (AOT, custom dispatch)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-17'
  source: official
  tags: triton,gpu,compile,aot,tooling,command-line,programming-model
---

# triton.compile — programmatic / ahead-of-time compilation

`triton.compile` compiles a `@triton.jit` kernel to a launchable artifact
(bound to a specific specialization + device) without going through the autotune
hot path. Use it for ahead-of-time (AOT) compilation, custom dispatch, caching
specialized binaries, or driving `num_warps`/`num_stages` explicitly.

## When to use it

- AOT: pre-compile a known kernel × shape set and ship binaries, avoiding
  first-call compile cost.
- Custom dispatch: you want to pick a specialization at runtime and launch it
  yourself rather than via the decorated entry point.
- Explicit control: set `num_warps`/`num_stages`/`num_ctas` directly, bypassing
  autotune.

## Syntax

```python
import triton

src = triton.compiler.ASTSource(
    fn=my_jit_kernel,
    constexprs={'BLOCK': 128},
    signature={'x_ptr': '*fp16', 'N': 'i32'},
)
compiled = triton.compile(src, num_warps=4, num_stages=3)
# compiled.metadata, compiled.kernel(...) available
```

`ASTSource` (the modern API) takes the jit fn + a `signature` (arg → triton type
string) + `constexprs` (the `tl.constexpr` bindings).

## Inspecting the result

```python
compiled.metadata              # grid/launch metadata
compiled.asm                   # {'ttir','ttgir','llir','ptx','cubin'} dict
# Save the binary / IR for reuse (pair with TRITON_KERNEL_DUMP_DIR + triton-opt)
open('kernel.ptx','w').write(compiled.asm['ptx'])
```

## Command-line / scripting

Compilation artifacts are also reachable by driving the compiler from a small
script and reading `compiled.asm` — useful in build pipelines that want to ship
PTX/CUBIN or diff IR between versions (see [triton-opt](../triton-opt/DOC.md)).

## Common pitfalls

- **Signature must match exactly.** A wrong type string (`'i64'` vs `'i32'`) or a
  missing `constexpr` silently selects a different specialization than your
  runtime kernel — diff the resulting IR if unsure.
- **Device/target binding.** A compiled artifact is specialized to a target
  (architecture + features); it is not portable across GPUs the way source is.
- **This bypasses autotune.** If your kernel is `@triton.autotune`'d, calling
  `triton.compile` on it compiles *a* specialization, it does not reproduce the
  tuned-best selection. Tune first, then AOT-compile the winner.

## Triton Version

Triton 2.1+ (`ASTSource` is the current API; older code uses a positional form).

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU.

## Related Instructions

- [triton-autotune](../triton-autotune/DOC.md)
- [triton-opt](../triton-opt/DOC.md)
- [triton-env-vars](../triton-env-vars/DOC.md)

## Example

```python
import triton, triton.language as tl

@triton.jit
def axpy(x_ptr, y_ptr, out_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid*BLOCK + tl.arange(0, BLOCK)
    mask = offs < N
    x = tl.load(x_ptr+offs, mask=mask)
    y = tl.load(y_ptr+offs, mask=mask)
    tl.store(out_ptr+offs, 2.0*x + y, mask=mask)

src = triton.compiler.ASTSource(
    fn=axpy,
    constexprs={'BLOCK': 256},
    signature={'x_ptr':'*fp32','y_ptr':'*fp32','out_ptr':'*fp32','N':'i32'},
)
compiled = triton.compile(src, num_warps=4, num_stages=2)
grid = lambda meta: ((N + 256 - 1)//256,)
compiled[grid](x, y, out, N)        # launch the AOT-compiled kernel
```
