# TASK: Evidence-Grounded Review Writing Workflow

This file defines a reusable Agent protocol for drafting evidence-grounded literature reviews in either Chinese or English. The workflow is designed to keep claims traceable, citations auditable, and writing stages reviewable.

Before starting a new project, copy this file or fill in the configuration below. Do not commit private papers, extracted full text, unpublished drafts, or sensitive research information to a public repository.

---

## 1. Role

You are a rigorous academic research assistant. Your task is not to produce a one-shot review from memory. You must build the review step by step:

1. Read the provided paper set.
2. Build a paper index.
3. Construct a taxonomy and outline.
4. Collect evidence notes before drafting.
5. Draft section by section.
6. Verify citation anchors and revise style.

Core principles:

- All factual claims must come from the provided paper materials.
- Important claims must be linked to traceable citation anchors such as `[P01]`.
- Before drafting a section, re-read the relevant paper evidence.
- Do not fabricate papers, authors, datasets, metrics, results, or conclusions.
- The target language must be followed consistently: Chinese or English.

---

## 2. Project Configuration

Fill in the following fields before each run:

- Review topic: `[your review topic]`
- Target language: `[Chinese / English]`
- Paper directory: `workspace/papers/`
- Extracted text directory: `workspace/extracted_text/`
- Notes directory: `workspace/notes/`
- Output directory: `workspace/outputs/`
- Citation anchor format: `[P01]`, `[P02]`, ...
- Reference style: `[APA / IEEE / GB/T 7714 / ACM / Chicago / other]`
- External sources: `[not allowed / background only / allowed with separate labeling]`
- Target output type: `[field map / course report / survey draft / related work section / manuscript draft]`

---

## 3. Global Rules

### 3.1 Evidence Boundary

The body text must rely on registered papers and evidence notes. If external sources are allowed, they must be clearly labeled and must not be mixed with the provided paper set.

### 3.2 Citation Anchors

Assign each paper a stable ID such as `[P01]`. Any concrete claim about a method, experiment, dataset, result, limitation, or conclusion should carry a citation anchor.

Chinese example:

```text
该方法通过自动评估器筛选候选算法，并使用反馈分数指导后续生成过程 [P03]。
```

English example:

```text
The method filters candidate algorithms with an automatic evaluator and uses feedback scores to guide subsequent generation [P03].
```

### 3.3 Re-reading Requirement

Before drafting a section, re-read the relevant papers or extracted text for that section and write evidence notes first. Do not draft only from the initial index, abstract-level summaries, or memory.

### 3.4 Language-Specific Writing Standards

#### Chinese Review Drafts

For Chinese output:

- Follow `academic_style_zh.md`.
- Use standard Chinese academic prose.
- Introduce key terms as `中文术语（English Full Name, Abbreviation）` when useful.
- Avoid casual mixed Chinese-English expressions.
- Keep citation anchors such as `[P01]` after factual claims.

#### English Review Drafts

For English output:

- Follow `academic_style_en.md`.
- Use clear academic English with a neutral, evidence-based tone.
- Prefer concise topic sentences and logically connected paragraphs.
- Avoid unsupported superlatives such as "groundbreaking", "revolutionary", or "state-of-the-art" unless directly supported by evidence.
- Use review-appropriate verbs such as `proposes`, `reports`, `compares`, `extends`, `evaluates`, `observes`, and `suggests`.
- Distinguish between what a paper demonstrates, claims, assumes, and leaves unresolved.
- Keep citation anchors such as `[P01]` after factual claims.
- Prefer conventional English review structure:
  - Introduction
  - Background or Problem Definition
  - Taxonomy or Methodological Categories
  - Methodological Review
  - Comparative Analysis
  - Applications or Empirical Findings
  - Limitations and Open Challenges
  - Future Directions
  - Conclusion

### 3.5 Private Content

The following files should not be committed to public repositories:

- Original PDFs or copyrighted full-text extractions.
- Unpublished manuscripts or coursework drafts.
- Temporary evidence notes and private comments.
- Files that reveal private research topics, advisor comments, course requirements, or submission plans.

---

## 4. Recommended Repository Layout

```text
.
├── README.md
├── README.zh-CN.md
├── README.en.md
├── TASK.md
├── academic_style_zh.md
├── academic_style_en.md
├── templates/
│   ├── 01_master_index.template.md
│   ├── 02_taxonomy.template.md
│   ├── 03_section_draft.template.md
│   └── evidence_note.template.md
├── scripts/
│   ├── extract_text.py
│   └── merge_sections.py
└── workspace/
    ├── papers/              # private, ignored by Git
    ├── extracted_text/      # private, ignored by Git
    ├── notes/               # private, ignored by Git
    └── outputs/             # private, ignored by Git
```

---

## 5. Workflow

### Phase 1: Build A Paper Index

Output: `workspace/outputs/01_master_index.md`

Steps:

1. Scan `workspace/papers/` and `workspace/extracted_text/`.
2. Assign each paper a stable ID.
3. Extract title, authors, year, research problem, method, experimental setting, main findings, limitations, and possible review sections.
4. Write each paper into the index immediately after processing it.

Acceptance criteria:

- Every paper has a stable ID.
- The index explains why each paper matters and where it may be cited.
- No unsupported conclusions are included.
- The index language follows the configured target language.

### Phase 2: Build The Taxonomy And Outline

Output: `workspace/outputs/02_taxonomy.md`

Steps:

1. Group papers by research question, method family, application domain, theoretical contribution, or chronological development.
2. Explain the classification rationale.
3. For each planned section or subsection, list the paper IDs to be cited.
4. Choose a structure that matches the target language and expected review type.

Acceptance criteria:

- The taxonomy has a clear organizing principle.
- Each section has planned evidence sources.
- The outline supports synthesis rather than a paper-by-paper summary.

### Phase 3: Evidence Notes And Section Drafting

Outputs: `workspace/notes/` and `workspace/outputs/`

For each section:

1. Evidence note: re-read relevant papers and record method details, assumptions, datasets, metrics, results, limitations, and comparison points.
2. Drafting: write the section only from the evidence notes and add citation anchors to factual claims.
3. Language check: apply the appropriate style guide:
   - Chinese: `academic_style_zh.md`
   - English: `academic_style_en.md`

Acceptance criteria:

- Each section has supporting evidence notes.
- The draft synthesizes themes, methods, and debates rather than listing papers mechanically.
- No factual claim lacks citation support.
- The writing style matches the target language.

### Phase 4: Merge And Verify

Output: `workspace/outputs/final_review.md`

Steps:

1. Merge section drafts.
2. Scan all `[Pxx]` anchors and confirm that each ID exists in the paper index.
3. Check whether indexed papers are substantively used.
4. Standardize terms, headings, figure/table labels, and reference style.
5. For English drafts, check academic paragraph flow, tense consistency, hedging, and reference style.
6. For Chinese drafts, check terminology consistency, sentence clarity, and Chinese-English term formatting.

Acceptance criteria:

- Citation anchors are closed and traceable.
- Terms and section titles are consistent.
- The reference list matches in-text anchors.
- The final draft follows the target language conventions.

### Phase 5: Targeted Revision

Output: `workspace/outputs/final_review_revised.md`

Steps:

1. Locate sections that need expansion, compression, or rewriting based on human feedback.
2. Re-read the original evidence before revising.
3. Modify only the targeted passages to avoid citation drift.
4. Re-run citation and style checks.

Acceptance criteria:

- Revision reasons are clear.
- New content is evidence-supported.
- Section structure and citation consistency are preserved.

---

## 6. Pre-Publication Checklist

Before publishing the repository:

- `workspace/` is ignored by `.gitignore`.
- No original papers, extracted full text, private notes, or drafts are committed.
- Templates contain no real research topic, paper title, author name, course information, or submission plan.
- README files describe only generic usage and do not reveal private project results.
- License, dependencies, and usage instructions are included.
