"""Merge private section drafts into a single manuscript file."""

from __future__ import annotations

import argparse
from pathlib import Path


def merge_sections(section_paths: list[Path], output_path: Path) -> None:
    chunks: list[str] = []

    for path in section_paths:
        chunks.append(path.read_text(encoding="utf-8").strip())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(chunks).strip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge markdown section drafts.")
    parser.add_argument("sections", nargs="+", type=Path, help="Section draft files in merge order.")
    parser.add_argument("-o", "--output", required=True, type=Path, help="Merged manuscript path.")
    args = parser.parse_args()

    merge_sections(args.sections, args.output)


if __name__ == "__main__":
    main()
