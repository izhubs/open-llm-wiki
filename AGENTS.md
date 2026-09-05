# AGENTS.md — Open LLM-Wiki Operating Constitution

This document defines the operating rules, data governance, and boundaries for AI agents working in this repository.

---

## 1. Core Principles

1. **Local-First & Model-Agnostic:** Knowledge lives in plain Markdown files. Any AI model (Claude, GPT, Gemini, local models) can read and write here without proprietary lock-in.
2. **Deterministic Governance:** AI operates under strict code rules. When in doubt, verify with scripts (`python scripts/check_docs.py`), not intuition.
3. **Anti-Spam File Policy:**
   - Never create ad-hoc task files or temporary markdown files in the root folder.
   - All structured knowledge belongs in `wiki/`.
   - All generated exports, reports, or data artifacts belong in `output/`.
4. **Direct Communication:** No flattering openers, no corporate roleplay ("Dear CEO", "I am delighted to..."). State facts, diffs, and actions directly.

---

## 2. Workspace Structure

```
.
├── AGENTS.md             # This constitution (read first)
├── MEMORY.md             # Project context and user preferences
├── README.md             # Repository documentation
├── .agent/
│   └── skills/           # Reusable skills and workflows
│       ├── doc_ingest/   # Ingest raw text/notes into structured wiki pages
│       └── doc_qc/       # Audit links, frontmatter, and orphan documents
├── scripts/
│   └── check_docs.py     # Zero-dependency Python document linter
├── wiki/                 # Primary knowledge base (plain Markdown)
│   ├── README.md         # Master index / table of contents
│   └── sample_sop.md     # Example structured SOP
└── output/               # Exports, generated deliverables, and reports
```

---

## 3. Mandatory Session Protocols

### 3.1 Startup Protocol
Whenever an AI agent starts a conversation or task in this repository:
1. Read `AGENTS.md` to load governance rules.
2. Read `MEMORY.md` to load user preferences and domain context.
3. Check `wiki/README.md` to understand existing topics before answering or creating new content.

### 3.2 Document Creation Standard
Every document in `wiki/` must begin with YAML frontmatter:

```markdown
---
id: doc_unique_slug
title: Document Title
type: concept | sop | research | decision
status: draft | verified | deprecated
tags: [tag1, tag2]
last_updated: YYYY-MM-DD
---
```

Rules:
- Filename must match the `id` (snake_case or kebab-case, lowercase only).
- Every document must be linked in `wiki/README.md` (no orphan documents).
- Cross-link related documents using Markdown links: `[Target Title](./target_file.md)`.

### 3.3 Quality Verification
Before finishing a session where files in `wiki/` were created or updated:
1. Run the validator:
   ```bash
   python scripts/check_docs.py
   ```
2. Resolve any reported errors (missing frontmatter, broken links, orphan documents).
