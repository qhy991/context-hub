#!/usr/bin/env python3
"""
Scrape HIP Runtime API Doxygen → context-hub DOC.md files.

Fetches function documentation from the HIP Doxygen pages at:
  https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group__*.html

Usage:
    python3 scrape_hip_api.py --outdir ../../content/rocm/docs
    python3 scrape_hip_api.py --outdir ../../content/rocm/docs --module Device
"""

import argparse
import os
import re
from datetime import date
from urllib.request import Request, urlopen

BASE_URL = "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html"

MODULES = [
    ("group___driver.html", "Initialization and Version"),
    ("group___device.html", "Device Management"),
    ("group___execution.html", "Execution Control"),
    ("group___error.html", "Error Handling"),
    ("group___stream.html", "Stream Management"),
    ("group___stream_m.html", "Stream Memory Operations"),
    ("group___event.html", "Event Management"),
    ("group___memory.html", "Memory Management"),
    ("group___peer_to_peer.html", "Peer to Peer Device Memory Access"),
    ("group___module.html", "Module Management"),
    ("group___occupancy.html", "Occupancy"),
    ("group___profiler.html", "Profiler Control"),
    ("group___clang.html", "Launch API"),
    ("group___texture.html", "Texture Management"),
    ("group___surface.html", "Surface Object"),
    ("group___runtime.html", "Runtime Compilation"),
    ("group___graph.html", "Graph Management"),
    ("group___virtual.html", "Virtual Memory Management"),
    ("group___graphics_interop.html", "Graphics Interoperability"),
    ("group___callback.html", "Callback Activity APIs"),
    ("group___external.html", "External Resource Interoperability"),
    ("group___stream_o.html", "Stream Ordered Memory Allocator"),
    ("group___memory_m.html", "Managed Memory"),
    ("group___memory_d.html", "Memory Management (Deprecated)"),
    ("group___driver_types.html", "Driver Types"),
    ("group___global_defs.html", "Global Enums and Defines"),
    ("group___linker_types.html", "JIT Linker Data Types"),
    ("group___context.html", "Context Management (Deprecated)"),
    ("group___module_cooperative_g.html", "Cooperative Groups Launch"),
    ("group___texture_d.html", "Texture Management (Deprecated)"),
]

RETURN_TYPES = (
    r"hipError_t|void|int|char|size_t|unsigned\s+int|unsigned\s+long|"
    r"long|float|double|bool|hipDevice_t|hipStream_t|hipEvent_t|"
    r"hipModule_t|hipFunction_t|hipGraph_t|hipGraphExec_t|"
    r"hipMemPool_t|hipArray_t|const\s+char\s*\*"
)


def fetch_url(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def discover_functions(html: str) -> list[tuple[str, str]]:
    """Return (anchor_id, function_name) pairs from a module page."""
    pattern = re.compile(
        r'href="[^"]+#(ga[a-f0-9]+)">(hip[A-Za-z0-9_]+)</a>'
    )
    seen: set[str] = set()
    results: list[tuple[str, str]] = []
    for anchor, name in pattern.findall(html):
        if name in seen:
            continue
        seen.add(name)
        results.append((anchor, name))
    return results


def extract_memdoc(html: str, anchor: str) -> str:
    match = re.search(
        rf'id="{re.escape(anchor)}".*?<div class="memdoc">(.*?)</div>\s*</div>',
        html,
        re.DOTALL,
    )
    return match.group(1) if match else ""


def extract_signature(html: str, anchor: str, name: str) -> str:
    escaped = re.escape(name)
    row_match = re.search(
        rf'<tr class="memitem[^"]*"[^>]*id="r_{re.escape(anchor)}".*?</tr>',
        html,
        re.DOTALL,
    )
    if row_match:
        row = row_match.group(0)
        ret_match = re.search(
            rf"(({RETURN_TYPES})\s*\**)\s*</td><td class=\"memItemRight\"",
            row,
            re.DOTALL,
        )
        args_match = re.search(rf">{escaped}</a>\s*\(([^)]*)\)", row)
        if ret_match and args_match:
            ret = strip_html(ret_match.group(1))
            args = strip_html(args_match.group(1))
            return f"{ret} {name}({args})"

    patterns = [
        rf'id="{re.escape(anchor)}".*?<div class="memtitle">.*?'
        rf"(({RETURN_TYPES})\s+\**\s*{escaped}\s*\([^)]*\))",
        rf"(({RETURN_TYPES})\s+\**\s*{escaped}\s*\([^)]*\))",
        rf">{escaped}</a>\s*\(([^)]*)\)",
    ]
    for pattern in patterns:
        match = re.search(pattern, html, re.DOTALL)
        if not match:
            continue
        if pattern.endswith(r"\(([^)]*)\)"):
            args = strip_html(match.group(1))
            return f"hipError_t {name}({args})"
        sig = strip_html(match.group(1))
        return re.sub(r"\s+", " ", sig)
    return ""


def parse_memdoc(memdoc: str) -> dict:
    description = ""
    paragraphs = re.findall(r"<p>(.*?)</p>", memdoc, re.DOTALL)
    if paragraphs:
        description = strip_html(paragraphs[0])

    params: list[dict] = []
    for row in re.finditer(
        r'<tr><td class="paramdir">(.*?)</td><td class="paramname">(.*?)</td><td>(.*?)</td></tr>',
        memdoc,
        re.DOTALL,
    ):
        params.append(
            {
                "direction": strip_html(row.group(1)),
                "name": strip_html(row.group(2)),
                "desc": strip_html(row.group(3)),
            }
        )

    return_desc = ""
    ret_match = re.search(
        r'<dl class="section return">.*?<dd>(.*?)</dd>',
        memdoc,
        re.DOTALL,
    )
    if ret_match:
        return_desc = strip_html(ret_match.group(1))

    see_also: list[str] = []
    see_match = re.search(
        r'<dl class="section see">.*?<dd>(.*?)</dd>',
        memdoc,
        re.DOTALL,
    )
    if see_match:
        see_also = re.findall(
            r'<a class="el" href="[^"]+">(hip[A-Za-z0-9_]+)</a>',
            see_match.group(1),
        )

    notes = [strip_html(p) for p in paragraphs[1:] if strip_html(p)]

    return {
        "description": description,
        "params": params,
        "return_desc": return_desc,
        "see_also": see_also,
        "notes": notes,
    }


def parse_api_page(html: str) -> list[dict]:
    functions: list[dict] = []
    for anchor, name in discover_functions(html):
        memdoc = extract_memdoc(html, anchor)
        parsed = parse_memdoc(memdoc) if memdoc else {
            "description": "",
            "params": [],
            "return_desc": "",
            "see_also": [],
            "notes": [],
        }
        signature = extract_signature(html, anchor, name)
        if not parsed["description"] and signature:
            parsed["description"] = f"{name} HIP Runtime API function."

        functions.append(
            {
                "name": name,
                "anchor": anchor,
                "signature": signature,
                **parsed,
            }
        )
    return functions


def scrape_module(module_path: str, module_name: str) -> list[dict]:
    url = f"{BASE_URL}/{module_path}"
    print(f"  Fetching: {module_name} ({url})")
    try:
        html = fetch_url(url)
    except Exception as exc:
        print(f"  ERROR fetching {url}: {exc}")
        return []

    functions = parse_api_page(html)
    for func in functions:
        func["module"] = module_name
        func["source_url"] = f"{url}#{func['anchor']}"

    with_params = sum(1 for f in functions if f["params"])
    with_sig = sum(1 for f in functions if f["signature"])
    print(
        f"    Found {len(functions)} functions "
        f"({with_sig} signatures, {with_params} with parameters)"
    )
    return functions


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def generate_doc_md(func: dict, today: str) -> str:
    name = func["name"]
    slug = f"hip-{name.lower()}"
    desc = func.get("description") or f"{name} HIP Runtime API function"
    module_slug = func.get("module", "").lower().replace(" ", "-")
    tags = f"rocm,gpu,hip,runtime-api,{module_slug}"

    # Classify the symbol so consumers can filter callable functions from
    # enums / flags / opaque typedefs.
    if func.get("signature") or func.get("params"):
        symbol_kind = "function"
    elif name.endswith("_t"):
        symbol_kind = "typedef"
    else:
        symbol_kind = "enum"

    sig_md = ""
    if func.get("signature"):
        sig_md = f"\n## Signature\n\n```c\n{func['signature']};\n```\n"

    params_md = ""
    if func.get("params"):
        params_md = "\n## Parameters\n\n"
        params_md += "| Direction | Parameter | Description |\n"
        params_md += "|-----------|-----------|-------------|\n"
        for param in func["params"]:
            params_md += (
                f"| {param.get('direction', '')} | `{param['name']}` | "
                f"{param.get('desc', '')} |\n"
            )

    return_md = ""
    if func.get("return_desc"):
        return_md = f"\n## Returns\n\n{func['return_desc']}\n"

    notes_md = ""
    if func.get("notes"):
        notes_md = "\n## Notes\n\n"
        for note in func["notes"]:
            notes_md += f"- {note}\n"

    see_md = ""
    if func.get("see_also"):
        see_md = "\n## See Also\n\n"
        for item in func["see_also"]:
            see_md += f"- {item}\n"

    return f"""---
name: {slug}
description: "{yaml_escape(desc)}"
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 2
  updated-on: '{today}'
  source: official
  tags: {tags}
  isa_category: runtime
  instruction_type: API
  symbol_kind: {symbol_kind}
  hw_unit: driver
  api_module: {func.get('module', '')}
---

# {name}

{desc}
{sig_md}{params_md}{return_md}{notes_md}{see_md}
## References

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)
- [HIP API Documentation]({func.get('source_url', '')})
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape HIP API Doxygen → DOC.md")
    parser.add_argument(
        "--outdir",
        default="../../content/rocm/docs",
        help="Output directory",
    )
    parser.add_argument(
        "--module",
        default=None,
        help="Only scrape modules whose name contains this substring",
    )
    args = parser.parse_args()

    out_dir = os.path.abspath(args.outdir)
    os.makedirs(out_dir, exist_ok=True)
    today = date.today().isoformat()

    modules = MODULES
    if args.module:
        modules = [
            (path, name)
            for path, name in MODULES
            if args.module.lower() in name.lower()
        ]

    all_functions: list[dict] = []
    seen_names: set[str] = set()

    for module_path, module_name in modules:
        funcs = scrape_module(module_path, module_name)
        for func in funcs:
            if func["name"] in seen_names:
                continue
            seen_names.add(func["name"])
            all_functions.append(func)

    print(f"\nTotal unique functions: {len(all_functions)}")

    for func in all_functions:
        slug = f"hip-{func['name'].lower()}"
        doc_dir = os.path.join(out_dir, slug)
        os.makedirs(doc_dir, exist_ok=True)
        doc_path = os.path.join(doc_dir, "DOC.md")
        with open(doc_path, "w", encoding="utf-8") as handle:
            handle.write(generate_doc_md(func, today))

    with_params = sum(1 for f in all_functions if f["params"])
    with_sig = sum(1 for f in all_functions if f["signature"])
    print(
        f"Generated {len(all_functions)} DOC.md files in {out_dir} "
        f"({with_sig} signatures, {with_params} with parameters)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
