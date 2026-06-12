#!/usr/bin/env bash
# Refresh CDNA ISA docs with per-architecture availability tags.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SPECDIR="${1:-/tmp/amdgpu_isa_specs}"
OUTDIR="$ROOT/content/rocm/docs"

bash "$(dirname "$0")/download_isa_xml.sh" "$SPECDIR"

echo "Removing stale ISA docs before refresh"
find "$OUTDIR" -maxdepth 1 -type d -name 'isa-*' -exec rm -rf {} +

for arch in cdna1 cdna2 cdna3 cdna4; do
  echo "Parsing amdgpu_isa_${arch}.xml"
  python3 "$(dirname "$0")/parse_isa_xml.py" \
    --xml "$SPECDIR/amdgpu_isa_${arch}.xml" \
    --outdir "$OUTDIR"
done

python3 "$(dirname "$0")/validate.py"
