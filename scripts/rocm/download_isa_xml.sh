#!/usr/bin/env bash
# Download latest AMD machine-readable ISA XML bundle from GPUOpen.
set -euo pipefail

OUTDIR="${1:-/tmp/amdgpu_isa_specs}"
mkdir -p "$OUTDIR"
ZIP="$OUTDIR/amdgpu_isa_latest.zip"

curl -fsSL "https://gpuopen.com/download/machine-readable-isa/latest/" -o "$ZIP"
unzip -o "$ZIP" -d "$OUTDIR"
ls -lh "$OUTDIR"/amdgpu_isa_cdna*.xml
