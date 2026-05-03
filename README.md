<div align="center">

# Evidence-Grounded Review Workflow

**A bilingual Agent workflow for evidence-grounded Chinese and English literature review drafting**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![Workflow](https://img.shields.io/badge/Workflow-Agent--Ready-2ea44f.svg)](TASK.md)
[![Privacy](https://img.shields.io/badge/Privacy-workspace%20ignored-important.svg)](.gitignore)

English | [简体中文](README.zh-CN.md)

</div>

## What Is This?

This repository provides a reusable Agent workflow for drafting evidence-grounded literature reviews in Chinese or English from a user-provided paper set.

Instead of asking an AI model to write from memory, the workflow guides an Agent to read your papers, build a paper index, construct a taxonomy, collect evidence notes, draft sections, and verify citation anchors such as `[P01]` and `[P02]`.

It is designed for researchers, students, and curious readers who want to quickly form a reliable first-pass understanding of a field: current progress, major schools of thought, method families, open problems, and future directions.

## Why Use It?

- **Paper-first**: the Agent works from your local papers, not vague model memory.
- **Traceable**: factual claims are linked to stable paper IDs.
- **Bilingual review drafting**: supports Chinese and English literature review drafts.
- **Language-aware style guides**: includes separate academic style guidance for Chinese and English.
- **Stage-based**: index, taxonomy, evidence notes, section drafts, and final merge.
- **Privacy-aware**: papers, extracted text, notes, and manuscripts stay in `workspace/`, which is ignored by Git.

## Quick Start

```bash
pip install -r requirements.txt
```

Put your PDFs here:

```text
workspace/papers/
```

Extract text from a PDF:

```bash
python scripts/extract_text.py workspace/papers/paper_01.pdf workspace/extracted_text/paper_01.txt
```

## Start The Workflow

First enter the repository directory:

```bash
cd path/to/evidence-grounded-review-workflow
```

Then start your preferred Agent tool and paste the workflow prompt below.

Common entry points:

```bash
# Cursor
# Open this folder in Cursor, then use Agent mode in the chat panel.

# Claude Code
claude

# Gemini CLI
gemini

# Codex CLI
codex
```

Use `Target language: English` for an English review draft:

```text
Read @TASK.md and follow Phase 1 to Phase 5.

My review topic is: "[your topic here]".
Use only the papers and extracted text under workspace/ as evidence.
Target language: English.
Write the review draft in English.

Outputs:
1. Create workspace/outputs/01_master_index.md.
2. Create workspace/outputs/02_taxonomy.md.
3. Save evidence notes under workspace/notes/.
4. Save section drafts under workspace/outputs/.
5. Merge the final draft to workspace/outputs/final_review.md.
6. Add [Pxx] citation anchors to all factual claims.
7. Follow @academic_style_en.md for English academic writing conventions.
```

Use `Target language: Chinese` for a Chinese review draft. See the full examples in [README.en.md](README.en.md) and [README.zh-CN.md](README.zh-CN.md).

## Repository Layout

```text
.
├── README.md
├── README.zh-CN.md
├── README.en.md
├── TASK.md
├── academic_style_zh.md
├── academic_style_en.md
├── requirements.txt
├── scripts/
│   ├── extract_text.py
│   └── merge_sections.py
├── templates/
│   ├── 01_master_index.template.md
│   ├── 02_taxonomy.template.md
│   ├── 03_section_draft.template.md
│   └── evidence_note.template.md
└── workspace/
    ├── papers/
    ├── extracted_text/
    ├── notes/
    └── outputs/
```

## Privacy Notice

Do not commit private research materials:

- Original PDFs.
- Extracted full text.
- Evidence notes.
- Unpublished review drafts.
- Any file that reveals private research topics, course requirements, advisor comments, or submission plans.

`workspace/` is ignored by default.

## Documentation

- [English Documentation](README.en.md)
- [中文说明文档](README.zh-CN.md)
- [Agent Task Protocol](TASK.md)
- [English Academic Style Guide](academic_style_en.md)
- [中文学术表达规则](academic_style_zh.md)

## License

MIT
