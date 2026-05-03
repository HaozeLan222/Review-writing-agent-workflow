"""Extract text from PDF files for private local review workflows.

This script is intentionally small and generic. Extracted text may contain
copyrighted material, so keep the output directory out of version control.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pdfplumber


def extract_pdf(pdf_path: Path, output_path: Path, max_pages: int | None = None) -> None:
    pages: list[str] = []

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        limit = total_pages if max_pages is None else min(max_pages, total_pages)

        for index in range(limit):
            text = pdf.pages[index].extract_text() or ""
            pages.append(f"\n\n--- Page {index + 1} ---\n\n{text}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(pages).strip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract PDF text into a local private text file.")
    parser.add_argument("pdf", type=Path, help="Path to the source PDF.")
    parser.add_argument("output", type=Path, help="Path to the output text file.")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Optional maximum number of pages to extract. Defaults to all pages.",
    )
    args = parser.parse_args()

    extract_pdf(args.pdf, args.output, args.max_pages)


if __name__ == "__main__":
    main()
