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
import json
from datetime import date
from pathlib import Path
from urllib.request import urlopen, Request
from html.parser import HTMLParser

BASE_URL = "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html"

# Key API modules to scrape
MODULES = [
    ("group___hip.html", "Initialization and Version"),
    ("group___device.html", "Device Management"),
    ("group___execution.html", "Execution Control"),
    ("group___error.html", "Error Handling"),
    ("group___stream.html", "Stream Management"),
    ("group___stream_mem.html", "Stream Memory Operations"),
    ("group___event.html", "Event Management"),
    ("group___memory.html", "Memory Management"),
    ("group___memory_deprecated.html", "Memory Management (Deprecated)"),
    ("group___external.html", "External Resource Interoperability"),
    ("group___s_o_m_a.html", "Stream Ordered Memory Allocator"),
    ("group___managed.html", "Managed Memory"),
    ("group___virtual_mem.html", "Virtual Memory Management"),
    ("group___texture.html", "Texture Management"),
    ("group___surface.html", "Surface Object"),
    ("group___peer.html", "Peer to Peer Device Memory Access"),
    ("group___module.html", "Module Management"),
    ("group___occupancy.html", "Occupancy"),
    ("group___profiler.html", "Profiler Control"),
    ("group___launch.html", "Launch API"),
    ("group___runtime_compiler.html", "Runtime Compilation"),
    ("group___graph.html", "Graph Management"),
    ("group___graphics_interop.html", "Graphics Interoperability"),
    ("group___c_g.html", "Cooperative Groups"),
]


def fetch_url(url: str) -> str:
    """Fetch URL content with proper headers."""
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


class APIFuncParser(HTMLParser):
    """Parse Doxygen HTML to extract function documentation."""

    def __init__(self):
        super().__init__()
        self.functions = []
        self.current_func = None
        self.state = None  # 'name', 'description', 'param_name', 'param_desc', 'return'
        self.capture = ""
        self.in_member = False
        self.in_heading = False
        self.current_heading = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Detect function member definitions
        if tag == "a" and "id" in attrs_dict:
            anchor = attrs_dict["id"]
            if anchor.startswith("ga") or anchor.startswith("gad"):
                if self.current_func:
                    self.functions.append(self.current_func)
                self.current_func = {
                    "id": anchor,
                    "name": "",
                    "description": "",
                    "signature": "",
                    "params": [],
                    "return_desc": "",
                }
                self.in_member = True

        # Detect headings
        if tag in ("h2", "h3", "h4") and self.in_member:
            cls = attrs_dict.get("class", "")
            if "memtitle" in cls or "memberdecl" in cls:
                self.in_heading = True

        # Parameter table cells
        if tag == "td" and self.in_member:
            cls = attrs_dict.get("class", "")
            if "paramname" in cls:
                self.state = "param_name"
                self.capture = ""
            elif "paramdesc" in cls:
                self.state = "param_desc"
                self.capture = ""

        # Return value section
        if tag == "p" and self.in_member:
            self.state = "text"
            self.capture = ""

    def handle_endtag(self, tag):
        if tag in ("h2", "h3", "h4"):
            self.in_heading = False
            if self.current_func and self.state == "name":
                self.current_func["name"] = self.capture.strip()
                self.state = None

        if tag == "td":
            if self.state == "param_name" and self.current_func:
                self.current_func["params"].append({"name": self.capture.strip(), "desc": ""})
            elif self.state == "param_desc" and self.current_func:
                if self.current_func["params"]:
                    self.current_func["params"][-1]["desc"] = self.capture.strip()
            self.state = None

    def handle_data(self, data):
        if self.in_heading and self.current_func:
            self.capture += data


def parse_api_page(html: str) -> list[dict]:
    """Extract function entries from a Doxygen module page."""
    functions = []

    # Strategy: find all function anchors and extract surrounding content
    # Doxygen pattern: <a id="ga..."> anchor near function docs
    # More reliable: find function signatures in code blocks

    # Find function names via pattern: hipFuncName(
    func_pattern = re.compile(r'\b(hip[A-Z][a-zA-Z0-9]*)\s*\(', re.MULTILINE)
    names = list(dict.fromkeys(func_pattern.findall(html)))

    # For each function, extract the section around it
    for name in names:
        func = {
            "name": name,
            "description": "",
            "params": [],
            "return_desc": "",
            "signature": "",
        }

        # Try to find description after the function name
        # Pattern: function name, then some text before the next function
        escaped = re.escape(name)
        desc_match = re.search(
            rf'{escaped}\s*\([^)]*\)[^<]*</code>\s*</td>\s*</tr>\s*</table>\s*<p[^>]*>(.*?)(?:</p>|<a id=)',
            html, re.DOTALL
        )
        if desc_match:
            desc = desc_match.group(1)
            # Clean HTML tags
            desc = re.sub(r'<[^>]+>', '', desc)
            desc = re.sub(r'\s+', ' ', desc).strip()
            if len(desc) > 500:
                desc = desc[:500] + "..."
            func["description"] = desc

        # Try to find full signature
        sig_pattern = re.compile(
            rf'(?:hipError_t|void|int|char|size_t|hipDevice_t|hipStream_t|hipEvent_t)\s+\**\s*{escaped}\s*\([^)]*\)',
            re.MULTILINE
        )
        sig_match = sig_pattern.search(html)
        if sig_match:
            func["signature"] = sig_match.group(0).strip()

        functions.append(func)

    return functions


def scrape_module(module_path: str, module_name: str) -> list[dict]:
    """Scrape a single Doxygen module page."""
    url = f"{BASE_URL}/{module_path}"
    print(f"  Fetching: {module_name} ({url})")

    try:
        html = fetch_url(url)
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return []

    functions = parse_api_page(html)
    for f in functions:
        f["module"] = module_name
        f["source_url"] = url

    print(f"    Found {len(functions)} functions")
    return functions


def generate_doc_md(func: dict, today: str) -> str:
    """Generate DOC.md content for a HIP API function."""

    name = func["name"]
    slug = f"hip-{name.lower()}"
    desc = func.get("description", f"{name} HIP Runtime API function")
    if not desc:
        desc = f"{name} HIP Runtime API function"

    # Escape for YAML
    desc_escaped = desc.replace('"', '\\"').replace("\n", " ")

    # Module-based tags
    module_slug = func.get("module", "").lower().replace(" ", "-")
    tags = f"rocm,gpu,hip,runtime-api,{module_slug}"

    # Signature
    sig_md = ""
    if func.get("signature"):
        sig_md = f"\n## Signature\n\n```c\n{func['signature']};\n```\n"

    # Parameters
    params_md = ""
    if func.get("params"):
        params_md = "\n## Parameters\n\n"
        params_md += "| Parameter | Description |\n|-----------|-------------|\n"
        for p in func["params"]:
            params_md += f"| `{p['name']}` | {p.get('desc', '')} |\n"

    return f"""---
name: {slug}
description: "{desc_escaped}"
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'ROCm 5.0+'
  revision: 1
  updated-on: '{today}'
  source: official
  tags: {tags}
  isa_category: runtime
  instruction_type: API
  hw_unit: driver
  api_module: {func.get('module', '')}
---

# {name}

{desc}
{sig_md}
{params_md}
## See Also

- [HIP Runtime API Reference](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html)
- [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/)

## References

- [HIP API Documentation]({func.get('source_url', '')})
"""


def main():
    parser = argparse.ArgumentParser(description="Scrape HIP API Doxygen → DOC.md")
    parser.add_argument("--outdir", default="../../content/rocm/docs",
                        help="Output directory")
    parser.add_argument("--module", default=None,
                        help="Only scrape this module (e.g., 'Device')")
    args = parser.parse_args()

    out_dir = os.path.abspath(args.outdir)
    os.makedirs(out_dir, exist_ok=True)
    today = date.today().isoformat()

    all_functions = []
    seen_names = set()

    modules = MODULES
    if args.module:
        modules = [(p, n) for p, n in MODULES if args.module.lower() in n.lower()]

    for module_path, module_name in modules:
        funcs = scrape_module(module_path, module_name)
        for f in funcs:
            if f["name"] not in seen_names:
                seen_names.add(f["name"])
                all_functions.append(f)

    print(f"\nTotal unique functions: {len(all_functions)}")

    # Generate DOC.md files
    for func in all_functions:
        slug = f"hip-{func['name'].lower()}"
        doc_dir = os.path.join(out_dir, slug)
        os.makedirs(doc_dir, exist_ok=True)

        doc_content = generate_doc_md(func, today)
        doc_path = os.path.join(doc_dir, "DOC.md")
        with open(doc_path, "w") as f:
            f.write(doc_content)

    print(f"Generated {len(all_functions)} DOC.md files in {out_dir}")
    return 0


if __name__ == "__main__":
    exit(main())
