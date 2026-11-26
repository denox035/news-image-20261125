#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the bundled poster (entry.png) to the output directory.
Standard library only; no network access. The copy is byte-for-byte,
so repeated runs always produce identical output.
"""
import os
import shutil
import sys

ENTRY = "entry.png"
DEFAULT_OUT = "/output"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT)
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, ENTRY),
                    os.path.join(out_dir, ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
