#!/usr/bin/env python3
"""Verifies that every publication in _data/publications.yaml (that lists
La Cava as an author, matching the filter in _pages/papers.md) has a
matching PDF checked into assets/papers/. Filenames are derived with the
exact same logic as _includes/pub-single.html so this stays in sync with
what the site actually links to (and with Zotero's own "Rename Associated
File" convention: "{Author(s)} - {Year} - {Title, 50 chars}.pdf").

Usage:
    python3 scripts/check_publication_pdfs.py            # error on missing PDFs
    python3 scripts/check_publication_pdfs.py --list     # just list, exit 0

Requires PyYAML (``pip install pyyaml``).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
import publication_pdfs as pp  # noqa: E402


def main() -> int:
    missing = pp.missing_pdfs()
    list_only = "--list" in sys.argv[1:]
    papers_dir = pp.PAPERS_DIR.relative_to(pp.ROOT)

    if not missing:
        print(f"All {len(pp.cava_refs())} publication PDFs are present in {papers_dir}.")
        return 0

    plural = "s" if len(missing) != 1 else ""
    print(f"{len(missing)} publication{plural} missing a PDF in {papers_dir}:", file=sys.stderr)
    for pub in missing:
        print(f"  - [{pub['id']}] {pub['filename']}", file=sys.stderr)

    if not list_only:
        print("", file=sys.stderr)
        print(
            "Tip: python3 scripts/find_missing_pdfs.py will search your Zotero storage for candidates.",
            file=sys.stderr,
        )

    return 0 if list_only else 1


if __name__ == "__main__":
    sys.exit(main())
