#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
#
# rename.py — translate a third-party N64 hires texture pack (Reloaded,
# Smash Remix, etc.) into one the SSB64 PC port can load directly.
#
# This script is MIT and contains no Rice CRC32 code. It only does a
# dictionary lookup against `mapping.json` (produced by the GPL-side
# `build_mapping.py`). The mapping itself is pure data and is shippable
# under any license.
#
# The mapping JSON is keyed by the third-party pack's filename hash:
#   "<RiceCRC8>#<fmt>#<siz>"            -> "<ourHash8>"
#   "<RiceCRC8>#<fmt>#<siz>#<palCRC8>"  -> "<ourHash8>"   (CI textures)
#
# For each PNG in the input pack whose filename matches one of those
# keys, we copy/symlink it to
#   <out>/<same/sub/dir/as/source>/<ourHash>#<fmt>#<siz>_all.png
# i.e. the source pack's folder layout (Characters/, Stages/, Hacks/...)
# is preserved so the output stays browsable and diffable against the
# original. The port scans mods/ recursively and keys purely off the
# filename, so nesting is cosmetic to it — it binds the same either way.
#
# Usage:
#   python3 rename.py --mapping mapping.json \
#                     --pack ~/Downloads/SSB-Reloaded \
#                     --out  ~/Library/Application\ Support/BattleShip/mods/SSB-MIT \
#                     [--symlink]

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

# Same grammar GLideN64 dumps with — used by Reloaded and most other N64
# hires packs. Matches:
#   "<prefix>#<crc>#<fmt>#<siz>[#<palCRC>]_<fmtTag>.png"
PACK_NAME_RE = re.compile(
    r'^.*#([0-9A-Fa-f]{8})#([0-9])#([0-9])(?:#([0-9A-Fa-f]{8}))?_(\w+)\.png$',
    re.IGNORECASE,
)


def out_filename(our_hash: str, fmt: int, siz: int) -> str:
    """Filename layout the port's runtime parser accepts (port/hires/HiResPack.cpp).
    The trailing _all is decorative — the parser ignores tag/prefix."""
    return f'#{our_hash.upper()}#{fmt:X}#{siz:X}.png'


def main():
    ap = argparse.ArgumentParser(description='Rename a third-party N64 hires pack to SSB64-port keys.')
    ap.add_argument('--mapping', required=True, type=Path,
                    help='mapping.json produced by build_mapping.py')
    ap.add_argument('--pack', required=True, type=Path,
                    help='Source pack root (e.g. extracted Reloaded ZIP)')
    ap.add_argument('--out', required=True, type=Path,
                    help='Destination pack folder')
    ap.add_argument('--symlink', action='store_true',
                    help='Symlink PNGs instead of copying (smaller / faster but pack moves break links).')
    args = ap.parse_args()

    if not args.pack.is_dir():
        sys.exit(f'--pack must be a directory: {args.pack}')
    if not args.mapping.is_file():
        sys.exit(f'--mapping not found: {args.mapping}')

    mapping = json.loads(args.mapping.read_text())
    print(f'Loaded {len(mapping)} mapping entries from {args.mapping}')

    args.out.mkdir(parents=True, exist_ok=True)

    matched = unmatched = bad = 0
    for src in args.pack.rglob('*.png'):
        m = PACK_NAME_RE.match(src.name)
        if not m:
            bad += 1
            continue
        crc = int(m.group(1), 16)
        fmt = int(m.group(2))
        siz = int(m.group(3))
        pal = int(m.group(4), 16) if m.group(4) else None

        if pal is not None:
            key = f'{crc:08X}#{fmt:X}#{siz:X}#{pal:08X}'
        else:
            key = f'{crc:08X}#{fmt:X}#{siz:X}'

        our_hash = mapping.get(key)
        if our_hash is None:
            unmatched += 1
            continue

        # Mirror the source's folder layout under --out.
        rel_dir = src.parent.relative_to(args.pack)
        dst_dir = args.out / rel_dir
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / out_filename(our_hash, fmt, siz)
        if dst.exists() or dst.is_symlink():
            dst.unlink()
        if args.symlink:
            os.symlink(src.resolve(), dst)
        else:
            shutil.copyfile(src, dst)
        matched += 1

    total = matched + unmatched + bad
    print(f'Done. {matched} matched, {unmatched} no-mapping, {bad} unparseable. '
          f'Total PNGs scanned: {total}.')
    print(f'Output: {args.out}')


if __name__ == '__main__':
    main()
