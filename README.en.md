<div align="center">

# Evidence-Grounded Review Workflow

**An Agent workflow for turning a given paper set into a traceable Chinese literature review draft**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![Workflow](https://img.shields.io/badge/Workflow-Agent--Ready-2ea44f.svg)](TASK.md)
[![Privacy](https://img.shields.io/badge/Privacy-workspace%20ignored-important.svg)](.gitignore)

English | [简体中文](README.zh-CN.md)

</div>

## Overview

This project provides a reusable Agent workflow for researchers, students, and curious readers who want to quickly draft a Chinese literature review from a given set of papers.

The workflow does not ask the model to write from memory. Instead, it guides an Agent to read your papers, build a paper index, construct a taxonomy, collect evidence notes, draft sections, and verify citation anchors such as `[P01]` and `[P02]`.

Use it to form a reliable first-pass understanding of a research field: current progress, major schools of thought, method families, representative works, limitations, and future directions.

## When To Use It

Use this workflow when:

- You already have a set of papers and want a structured Chinese review draft.
- You are new to a field and want to understand its major directions.
- You need to organize multiple papers into a taxonomy, method comparison, and research outlook.
- You want AI-assisted writing with fewer hallucinations, fewer unsupported claims, and clearer citation tracking.
- You want an auditable intermediate process instead of a one-shot generated manuscript.

It is not intended for:

- Writing a full review without providing papers.
- Producing a submission-ready manuscript directly.
- Replacing human judgment about paper quality, novelty, or experimental reliability.

## Workflow

```text
Given papers
   |
Text extraction and reading
   |
Paper index [P01] [P02] ...
   |
Taxonomy and outline
   |
Evidence notes
   |
Section-by-section Chinese draft
   |
Citation closure and style revision
```

## Repository Layout

```text
.
├── README.md                       # GitHub landing page
├── README.zh-CN.md                 # Chinese documentation
├── README.en.md                    # English documentation
├── TASK.md                         # Agent task protocol
├── academic_style_zh.md            # Chinese academic style guide
├── requirements.txt
├── scripts/
│   ├── extract_text.py             # PDF text extraction
│   └── merge_sections.py           # Markdown section merger
├── templates/
│   ├── 01_master_index.template.md
│   ├── 02_taxonomy.template.md
│   ├── 03_section_draft.template.md
│   └── evidence_note.template.md
└── workspace/                      # Private workspace, ignored by Git
    ├── papers/                     # Put original PDFs here
    ├── extracted_text/             # Extracted text files
    ├── notes/                      # Evidence notes
    └── outputs/                    # Index, taxonomy, drafts
```

`workspace/` is your private local workspace and is ignored by `.gitignore`. It can contain papers, extracted text, notes, and generated drafts, but should not be committed to a public repository.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Source Papers

Put your PDF files under:

```text
workspace/papers/
```

Recommended naming:

```text
workspace/papers/paper_01.pdf
workspace/papers/paper_02.pdf
workspace/papers/paper_03.pdf
```

### 3. Extract Text

Run this for each PDF:

```bash
python scripts/extract_text.py workspace/papers/paper_01.pdf workspace/extracted_text/paper_01.txt
```

For a quick preview, extract only the first few pages:

```bash
python scripts/extract_text.py workspace/papers/paper_01.pdf workspace/extracted_text/paper_01.txt --max-pages 5
```

For actual drafting, extract the full paper so the Agent does not rely only on abstracts.

### 4. Start An Agent

Open this repository in Cursor, Claude Code, Codex CLI, or another Agent environment that can read project files. Then send a prompt like:

```text
Read @TASK.md and follow Phase 1 to Phase 5.

My review topic is: "[your topic here]".
Use only the papers and extracted text under workspace/ as evidence.
Write the review draft in Chinese.

Requirements:
1. Create workspace/outputs/01_master_index.md first.
2. Then create workspace/outputs/02_taxonomy.md.
3. Before drafting each section, save evidence notes under workspace/notes/.
4. Save section drafts under workspace/outputs/.
5. Merge the final draft to workspace/outputs/final_review.md.
6. Add [Pxx] citation anchors to all factual claims.
```

If you only want to build the paper index first:

```text
Read @TASK.md. Only execute Phase 1 for now:
scan workspace/papers/ and workspace/extracted_text/,
build a paper index for all papers,
and save it to workspace/outputs/01_master_index.md.
Stop after Phase 1 and wait for my confirmation.
```

### 5. Check Outputs

Common output paths:

```text
workspace/outputs/01_master_index.md      # Paper index
workspace/outputs/02_taxonomy.md          # Taxonomy and outline
workspace/notes/                          # Evidence notes
workspace/outputs/sec_*.md                # Section drafts
workspace/outputs/final_review.md         # Merged review draft
```

### 6. Merge Sections

If the Agent generates multiple section files, merge them with:

```bash
python scripts/merge_sections.py workspace/outputs/sec_1.md workspace/outputs/sec_2.md workspace/outputs/sec_3.md -o workspace/outputs/final_review.md
```

## Practical Tips

- Start with 5 to 10 papers if this is your first run.
- Review each phase before moving to the next one.
- Verify critical metrics, experimental results, and method details against the original papers.
- Treat the result as a review draft and field map, not a submission-ready manuscript.
- If you publish this repository, publish only the workflow templates, not `workspace/`.

## Privacy And Copyright

This repository only contains a generic workflow, templates, and scripts. Do not publicly commit:

- Original PDFs.
- Extracted full text.
- Private evidence notes.
- Unpublished review drafts, coursework, or submission versions.
- Files that reveal private research topics, advisor comments, course requirements, or submission plans.

`.gitignore` ignores `workspace/`, `papers/`, `papers_txt/`, and common manuscript output files by default.

## License

MIT
