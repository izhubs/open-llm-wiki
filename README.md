# Open LLM-Wiki

[![CI](https://github.com/izhubs/open-llm-wiki/actions/workflows/ci.yml/badge.svg)](https://github.com/izhubs/open-llm-wiki/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A lightweight, local-first starter architecture for collaborative Human-AI knowledge management, inspired by Andrej Karpathy's LLM-Wiki pattern and hardened with enterprise data governance principles.

[Quick Start](#-quick-start-under-1-minute) · [Operator & Agent Guide](docs/USER_GUIDE.md) · [Why Open LLM-Wiki?](#️-why-open-llm-wiki) · [Document Schema](#-document-schema)

---

## 🌟 Philosophy

Most AI-assisted documentation setups fail due to **context drift** and **file sprawl**: agents generate loose files everywhere, forget conventions, and break internal links.

Open LLM-Wiki solves this with five core rules:

1. **Simple UX (< 10-Second Setup):** Zero external libraries, zero databases, zero build steps. Works out of the box with Python 3 and any AI coding assistant (Google Antigravity, Cursor, Claude Code, Windsurf, Aider).
2. **Own the Migration Moment:** Turn unstructured meeting notes, transcripts, and brain dumps into structured knowledge in minutes with the built-in `doc_ingest` skill.
3. **AI is the Operating Interface:** AI agents don't just read documents; they maintain the wiki index, cross-reference concepts, and keep links healthy following `AGENTS.md`.
4. **Indestructible Core:** A standalone, zero-dependency validation script (`scripts/check_docs.py`) acts as a deterministic gate against broken links, missing metadata, and orphan documents.
5. **100% Local-First Data Ownership:** All content is pure Markdown on your local file system. No proprietary cloud database, no vendor lock-in.

---

## ⚖️ Why Open LLM-Wiki?

| Feature | Heavy RAG (Vector DB / LangChain) | Manual Notes (Notion / Obsidian) | **Open LLM-Wiki** |
| :--- | :---: | :---: | :---: |
| **Setup Time** | Hours (Docker, embeddings, APIs) | Minutes | **< 10 seconds** (Zero dependencies) |
| **Context Overhead** | Bloated context window (>50k tokens) | N/A | **✅ Progressive Disclosure (< 40 tokens cold start)** |
| **Knowledge Quality** | Fragmented chunks, transient | High quality, but high human effort | **Compiled, structured, compounding** |
| **Anti-Spam Gate** | ❌ None | ❌ None | **✅ Python linter (`check_docs.py`)** |
| **Data Ownership** | Cloud / Vendor lock-in | Proprietary / Local | **✅ 100% Local Markdown on disk** |
| **Agent Curation** | Retrieval-only | Human-only | **✅ AI maintains index & links** |
| **License** | Complex / Commercial | Subscription / Freemium | **MIT (Free forever)** |

---

## 📂 Repository Structure

```
open-llm-wiki/
├── AGENTS.md             # Operating rules and boundaries for AI agents
├── MEMORY.md             # Project context and user preferences
├── README.md             # This guide
├── LICENSE               # MIT License
├── .agent/
│   └── skills/           # Modern skills with progressive disclosure (doc_ingest, doc_qc)
├── docs/
│   └── USER_GUIDE.md     # Comprehensive guide for humans & AI agents
├── scripts/
│   └── check_docs.py     # Standalone Python linter (zero dependencies)
├── wiki/                 # Knowledge vault (Markdown + YAML Frontmatter)
│   ├── README.md         # Master catalog / index
│   └── sample_sop.md     # Reference standard operating procedure
└── output/               # Exports, generated reports, and deliverables
```

---

## 🚀 Quick Start (Under 1 Minute)

### 1. Clone or Fork
```bash
git clone https://github.com/izhubs/open-llm-wiki.git my-wiki
cd my-wiki
```

### 2. Open with Your AI Assistant
Open the folder in your favorite AI environment (Google Antigravity, Cursor, Claude Code).

Prompt your AI:
> *"Read `AGENTS.md` and `MEMORY.md`, then list what documents currently exist in `wiki/`."*

### 3. Ingest Your First Document
Give your AI any raw text, notes, or transcript:
> *"Use the `doc_ingest` skill to convert this raw note into a structured SOP in `wiki/` and register it in `wiki/README.md`."*

### 4. Verify Document Integrity
Run the built-in validator at any time:
```bash
python scripts/check_docs.py
```

Expected output:
```text
Checking 2 document(s) in wiki...

Result: PASSED (2 files verified, 0 errors, 0 warning(s))
```

---

## 📋 Document Schema

Every file in `wiki/` must start with YAML frontmatter:

```markdown
---
id: sample_sop
title: Sample Standard Operating Procedure
type: sop               # concept | sop | research | decision
status: verified        # draft | verified | deprecated
tags: [template, sop]
last_updated: 2026-09-05
---
```

---

## 🛡️ License

Released under the [MIT License](./LICENSE). Free for personal, commercial, and open-source use.
