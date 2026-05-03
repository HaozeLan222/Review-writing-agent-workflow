<div align="center">

# Evidence-Grounded Review Workflow

**一个用于“给定论文集合 -> 中英文综述初稿”的证据驱动 Agent 工作流**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![Workflow](https://img.shields.io/badge/Workflow-Agent--Ready-2ea44f.svg)](TASK.md)
[![Privacy](https://img.shields.io/badge/Privacy-workspace%20ignored-important.svg)](.gitignore)

[English](README.en.md) | 简体中文

</div>

## 项目简介

本项目面向科研从业者、学生以及对某个研究方向感兴趣的读者，提供一套 **基于给定论文快速撰写中文或英文综述初稿** 的 Agent 工作流。

它的目标不是让模型“凭空写综述”，而是让 Agent 先阅读你提供的论文，建立文献索引和分类法，再进行证据摘记、分章节写作和引用核查。每个事实陈述都尽量通过 `[P01]`、`[P02]` 这样的引用锚点追踪到具体论文。

适合用它来快速初步了解一个领域的研究现状、主要流派、方法差异、代表性工作和潜在研究空白。你可以选择输出中文综述，也可以选择输出更符合英文论文写作习惯的 English literature review draft。

## 适用场景

- 你手头已经有一批论文，希望快速整理出中文或英文综述初稿。
- 你刚进入一个方向，想先可信地了解该领域有哪些主要方法流派。
- 你需要把多篇论文组织成“研究现状、分类法、方法对比、局限与展望”。
- 你希望 AI 辅助写作时尽量减少幻觉、错引和无来源判断。
- 你想保留一个可复查的中间过程，而不只是得到一篇不可追踪的生成稿。

不适合的场景：

- 没有提供论文，却希望生成完整学术综述。
- 需要直接产出可投稿终稿。
- 需要替代人工判断论文质量、创新性或实验可信度。

## 工作流概览

```text
给定论文
   ↓
文本抽取与阅读
   ↓
文献索引 [P01] [P02] ...
   ↓
分类法与章节大纲
   ↓
证据摘记
   ↓
分章节中英文综述初稿
   ↓
引用闭环与风格修订
```

## 目录结构

```text
.
├── README.md                       # GitHub 首页与语言入口
├── README.zh-CN.md                 # 中文说明
├── README.en.md                    # English documentation
├── TASK.md                         # Agent 执行协议
├── academic_style_zh.md            # 中文学术表达润色规则
├── academic_style_en.md            # 英文学术综述写作规则
├── requirements.txt
├── scripts/
│   ├── extract_text.py             # PDF 文本抽取脚本
│   └── merge_sections.py           # 章节合并脚本
├── templates/
│   ├── 01_master_index.template.md
│   ├── 02_taxonomy.template.md
│   ├── 03_section_draft.template.md
│   └── evidence_note.template.md
└── workspace/                      # 私有工作区，默认不提交
    ├── papers/                     # 放原始 PDF
    ├── extracted_text/             # 放抽取后的文本
    ├── notes/                      # 放证据摘记
    └── outputs/                    # 放索引、大纲和综述草稿
```

`workspace/` 是你的本地私有工作区，已经被 `.gitignore` 忽略。这里可以放论文、抽取文本、笔记和生成稿，但不要提交到公开仓库。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 放入原始论文

把你要综述的 PDF 论文放到：

```text
workspace/papers/
```

建议文件名保持可读，例如：

```text
workspace/papers/paper_01.pdf
workspace/papers/paper_02.pdf
workspace/papers/paper_03.pdf
```

### 3. 抽取论文文本

对每篇 PDF 执行：

```bash
python scripts/extract_text.py workspace/papers/paper_01.pdf workspace/extracted_text/paper_01.txt
```

如果只想先抽取前几页做快速预览，可以使用：

```bash
python scripts/extract_text.py workspace/papers/paper_01.pdf workspace/extracted_text/paper_01.txt --max-pages 5
```

正式写作时建议抽取完整论文，避免 Agent 只基于摘要写作。

### 4. 启动 Agent

先进入项目目录：

```bash
cd path/to/evidence-grounded-review-workflow
```

然后选择你正在使用的 Agent 工具。最稳妥的方式是进入交互模式后，把下面的启动提示词粘贴进去。

常见启动方式：

```bash
# Cursor
# 用 Cursor 打开本项目文件夹，然后在 Chat 面板切换到 Agent 模式。

# Claude Code
claude

# Gemini CLI
gemini

# Codex CLI
codex
```

不同 CLI 的参数可能会随版本变化，交互式启动最不容易出错。核心要求是：Agent 必须能读取当前项目里的 `TASK.md`、`academic_style_zh.md`、`academic_style_en.md`、`workspace/` 和 `templates/`。

如果要生成中文综述，把下面这段发给 Agent：

```text
请阅读 @TASK.md，并严格按照其中的 Phase 1 到 Phase 5 执行。

我的综述主题是：「在这里填写你的综述主题」。
请以 workspace/papers/ 和 workspace/extracted_text/ 中的论文材料为唯一事实来源，
目标语言：中文。
请用中文撰写综述初稿，并遵循 @academic_style_zh.md。

要求：
1. 先建立 workspace/outputs/01_master_index.md。
2. 再生成 workspace/outputs/02_taxonomy.md。
3. 每个章节写作前，先在 workspace/notes/ 中记录证据摘记。
4. 分章节输出到 workspace/outputs/。
5. 最终合并为 workspace/outputs/final_review.md。
6. 所有事实陈述必须带 [Pxx] 引用锚点。
```

如果要生成英文综述，把 `目标语言` 改成 English，并使用英文风格规则：

```text
Please read @TASK.md and strictly follow Phase 1 to Phase 5.

My review topic is: "[fill in your review topic here]".
Target language: English.
Use only the papers and extracted text under workspace/ as evidence.
Please draft an English literature review and follow @academic_style_en.md.

Requirements:
1. Create workspace/outputs/01_master_index.md first.
2. Then create workspace/outputs/02_taxonomy.md.
3. Before drafting each section, save evidence notes under workspace/notes/.
4. Save section drafts under workspace/outputs/.
5. Merge the final draft to workspace/outputs/final_review.md.
6. Add [Pxx] citation anchors to all factual claims.
7. Use neutral academic English, clear topic sentences, careful hedging, and review-appropriate structure.
```

语言选择只看提示词里的这一行：

```text
Target language: English.
```

或：

```text
目标语言：中文。
```

如果你只想先生成索引，不想一次写完整综述，可以这样启动：

```text
请阅读 @TASK.md。现在只执行 Phase 1：
遍历 workspace/papers/ 和 workspace/extracted_text/，
为每篇论文建立文献索引，并输出到 workspace/outputs/01_master_index.md。
完成后停止，等待我确认。
```

### 5. 查看输出

常见输出位置如下：

```text
workspace/outputs/01_master_index.md      # 文献索引
workspace/outputs/02_taxonomy.md          # 分类法与大纲
workspace/notes/                          # 每节写作前的证据摘记
workspace/outputs/sec_*.md                # 分章节草稿
workspace/outputs/final_review.md         # 合并后的综述初稿
```

### 6. 合并章节

如果 Agent 已经生成多个章节文件，可以用脚本合并：

```bash
python scripts/merge_sections.py workspace/outputs/sec_1.md workspace/outputs/sec_2.md workspace/outputs/sec_3.md -o workspace/outputs/final_review.md
```

## 使用建议

- 一次不要塞入过多论文。初次使用可以先从 15 到 20 篇开始。
- 每完成一个阶段，先人工检查再进入下一阶段。
- 对关键数据、实验结论和方法细节，务必回到原文确认。
- 把生成结果当作“综述初稿”和“领域地图”，不要直接当作可投稿终稿。
- 英文输出时，建议额外检查段落主题句、时态、hedging、术语缩写和目标期刊引用格式。
- 如果要公开项目，请只公开本仓库模板，不要公开 `workspace/`。

## 隐私与版权

本项目只提供通用 workflow、模板和脚本。请不要公开提交：

- 原始 PDF。
- 论文全文抽取文本。
- 私有证据摘记。
- 未发表综述稿、课程作业或投稿版本。
- 会暴露具体研究主题、导师要求、课程要求或投稿计划的内容。

`.gitignore` 已默认忽略 `workspace/`、`papers/`、`papers_txt/` 和常见 manuscript 输出文件。

## License

MIT
