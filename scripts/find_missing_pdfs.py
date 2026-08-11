#!/usr/bin/env python3
"""Helper for filling gaps found by check_publication_pdfs.py: only when a
publication's PDF is actually missing from assets/papers/ does this search
your local Zotero storage for a matching file. It never runs the scan
otherwise, since walking ~3,500 PDFs on every commit would be wasteful and
the storage path is local-only (not something a commit hook should depend
on). Matching is by author surname + overlapping title words, not just the
year, because Zotero attachments can be named from an epub-ahead-of-print
date that later drifts from the final `issued.year` in publications.yaml.

Usage:
    python3 scripts/find_missing_pdfs.py                # show candidates only
    python3 scripts/find_missing_pdfs.py --copy          # copy unambiguous matches
    python3 scripts/find_missing_pdfs.py --zotero-dir PATH

Requires PyYAML (``pip install pyyaml``).
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
import publication_pdfs as pp  # noqa: E402

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "into", "is", "it", "of", "on", "or", "that", "the", "to", "via",
    "with", "using", "towards", "toward",
}

_ET_AL_RE = re.compile(r" et al\.?$", re.IGNORECASE)
_AND_RE = re.compile(r" and ", re.IGNORECASE)
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def normalize_tokens(text: str) -> list[str]:
    normalized = _NON_ALNUM_RE.sub(" ", str(text).lower())
    return [w for w in normalized.split() if w not in STOPWORDS and len(w) > 2]


def surname_token(author_segment: str) -> str | None:
    first_author = _AND_RE.split(_ET_AL_RE.sub("", str(author_segment)))[0]
    tokens = _NON_ALNUM_RE.sub(" ", first_author.lower()).split()
    return tokens[-1] if tokens else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--copy", action="store_true")
    parser.add_argument("--zotero-dir", default=str(Path.home() / "Zotero" / "storage"))
    args = parser.parse_args()

    missing = pp.missing_pdfs()

    if not missing:
        print("No missing PDFs, nothing to search for. (Zotero storage was not scanned.)")
        return 0

    zotero_dir = Path(args.zotero_dir)
    if not zotero_dir.is_dir():
        print(f"Zotero storage dir not found: {zotero_dir}", file=sys.stderr)
        print("Pass --zotero-dir PATH to point at the right location.", file=sys.stderr)
        return 1

    print(f"{len(missing)} PDF(s) missing; searching {zotero_dir} ...", file=sys.stderr)
    candidates = [
        {"path": path, "tokens": normalize_tokens(path.stem)}
        for path in zotero_dir.glob("*/*.pdf")
    ]
    print(f"Scanned {len(candidates)} PDFs.\n", file=sys.stderr)

    for pub in missing:
        title_tokens = set(normalize_tokens(pub["title"]))
        surname = surname_token(pub["filename"].split(" - ")[0])

        scored = []
        for c in candidates:
            overlap = title_tokens & set(c["tokens"])
            if not overlap:
                continue

            surname_match = bool(surname) and any(surname in t for t in c["tokens"])
            if not surname_match and len(overlap) < 3:
                continue

            scored.append({"path": c["path"], "overlap": len(overlap), "surname_match": surname_match})

        scored.sort(key=lambda c: (not c["surname_match"], -c["overlap"]))

        print(f"[{pub['id']}]")
        print(f"  expected: {pub['filename']}")
        if not scored:
            print("  no candidates found")
        else:
            for i, c in enumerate(scored[:5]):
                marker = "->" if i == 0 else "  "
                print(f"  {marker} {c['path']}  (overlap={c['overlap']}, author_match={c['surname_match']})")

            if args.copy:
                top = scored[0]
                unambiguous = len(scored) == 1 or scored[1]["overlap"] < top["overlap"]
                if unambiguous and top["surname_match"]:
                    shutil.copy(top["path"], pub["path"])
                    print(f"  copied -> {pub['path']}")
                else:
                    print("  skipped copy: ambiguous match, resolve by hand")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
