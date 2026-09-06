# Open LLM-Wiki: Comprehensive Operator & Agent Guide

> A practical guide for humans managing knowledge and AI agents operating within this repository.

---

## 1. Mental Model: Compilation over Retrieval

Traditional Retrieval-Augmented Generation (RAG) treats knowledge as raw, fragmented chunks retrieved on the fly. This often causes high token consumption, slow response times, and inconsistent results.

**Open LLM-Wiki treats knowledge as compiled source code:**

```
[Raw Sources: Notes / Transcripts / Ideas]
                    │
                    ▼
          ┌──────────────────┐
          │  LLM Compiler    │ (via doc_ingest skill)
          └──────────────────┘
                    │
                    ▼
       ┌───────────────────────────┐
       │   wiki/*.md + YAML Meta   │ (Compiled Knowledge Vault)
       └───────────────────────────┘
                    ▲
                    │ (Zero-dependency validation)
          ┌──────────────────┐
          │ check_docs.py    │ (Deterministic Quality Gate)
          └──────────────────┘
```

- **Human Role:** Provide raw inputs, pose high-level questions, and make critical strategic decisions.
- **AI Agent Role:** Extract facts, standardize terminology, write YAML frontmatter, maintain bidirectional links, and keep the index clean.
- **Script Role (`check_docs.py`):** Act as the impartial judge, ensuring no broken links, orphan notes, or missing metadata slip into the repository.

---

## 2. Human Operator Playbook

### 2.1 Viewing Your Wiki with Obsidian (Recommended)
While any code editor works, [Obsidian](https://obsidian.md) provides a powerful visual interface:
1. Download and install Obsidian.
2. Click **Open folder as vault** and select your `open-llm-wiki` folder.
3. Open `wiki/README.md` as your homepage.
4. Press `Ctrl + G` (or `Cmd + G`) to open the interactive **Graph View** showing connections between concepts.

---

### 2.2 Ready-to-Use Copy-Paste Prompts

Copy and paste these prompts directly into your AI assistant (Google Antigravity, Cursor, Claude Code, Windsurf, Aider):

#### Recipe 1: Turn Messy Meeting Notes into an Actionable SOP
> *"Use the `doc_ingest` skill to convert this raw meeting note into a structured SOP. Save it under `wiki/`, assign a descriptive kebab-case ID, include YAML frontmatter with `type: sop`, add it to `wiki/README.md`, and run `scripts/check_docs.py` to verify."*
>
> *(Paste your raw notes below the prompt)*

#### Recipe 2: Summarize Technical Research or an Article
> *"Ingest this research article into `wiki/`. Summarize core principles, extract key trade-offs, link to any related documents already in `wiki/`, assign `type: research`, register it in `wiki/README.md`, and ensure `scripts/check_docs.py` passes."*

#### Recipe 3: Record an Architecture or Policy Decision (ADR)
> *"Record this technical decision into `wiki/`. Follow the decision schema: Context, Options Considered, Decision Made, Trade-offs, and Consequences. Assign `type: decision`, link it in `wiki/README.md`, and verify document integrity."*

#### Recipe 4: Routine Health Check & Link Audit
> *"Run `python scripts/check_docs.py`. If there are any broken links, orphan documents, or frontmatter errors, identify them, propose the exact fixes, and update the affected files."*

---

### 2.3 "Own the Migration Moment": Importing from Notion or Apple Notes
Migrating from your existing tool takes less than 2 minutes:
1. Export your notes from Notion, Obsidian, or Apple Notes as Markdown (`.md`) or plain text.
2. Place them temporarily in an `inbox/` or `raw/` folder at the root of the project.
3. Tell your AI:
   > *"Review all markdown files inside `inbox/`. One by one, ingest them into `wiki/` following the document schema in `AGENTS.md`. Cross-link related terms, update `wiki/README.md`, and clean up `inbox/` once completed."*

---

### 2.4 Separation of Raw Data vs. Compiled Knowledge
- **`wiki/` (Compiled Knowledge):** Only clean Markdown files with YAML frontmatter. **Zero binary blobs, zero large PDFs, zero raw HTML dumps.**
- **`output/` (Deliverables):** Generated reports, exported summaries, and artifacts for external sharing.
- **`raw/` (Optional Staging):** If you have large source PDFs, audio transcripts, or raw data, store them in a separate `raw/` folder (or external storage) and instruct the AI to ingest only distilled insights into `wiki/`.

---

## 3. AI Agent Operating Guidelines

When an AI agent operates in this repository, it must adhere to these deterministic workflows:

### 3.1 The 5-Step Ingestion Pipeline
1. **Classify:** Determine if the document is a `concept`, `sop`, `decision`, or `research`.
2. **Slugify:** Generate a unique lowercase identifier matching the filename (e.g., `slug: git_workflow` -> file: `wiki/git_workflow.md`).
3. **Format:** Prepend valid YAML frontmatter:
   ```yaml
   ---
   id: git_workflow
   title: Git Workflow & Branching Strategy
   type: sop
   status: draft
   tags: [git, workflow, engineering]
   last_updated: YYYY-MM-DD
   ---
   ```
4. **Index:** Add the document to `wiki/README.md` under its category. Never leave orphan documents.
5. **Verify:** Run `python scripts/check_docs.py` and confirm exit code 0 before concluding the task.

### 3.2 Knowledge Conflict Protocol
If new incoming information contradicts an existing wiki document:
- **Do not silently overwrite** existing truth.
- Flag the contradiction to the user: *"Document `wiki/pricing_model.md` specifies Tier A at $50/mo, but this new note states $80/mo. Should I update the existing document or record this as a new version?"*

---

## 4. Scaling Beyond 100 Documents

When your knowledge base grows beyond 100 files, keep the root `wiki/` index lightweight by introducing category subdirectories:

```
wiki/
├── README.md               # Master index referencing sub-indices
├── concepts/               # Domain models, glossary, entities
│   └── README.md
├── sops/                   # Repeatable standard procedures
│   └── README.md
├── decisions/              # Architecture Decision Records (ADRs)
│   └── README.md
└── research/               # Deep-dive benchmarks and technical notes
    └── README.md
```

The validation script `scripts/check_docs.py` natively traverses all nested subdirectories (`**/*.md`), allowing your wiki structure to scale seamlessly without code changes.

---

## 5. Troubleshooting Linter Errors

When `python scripts/check_docs.py` reports errors, use this quick resolution guide:

| Error Message | Cause | Resolution |
| :--- | :--- | :--- |
| `Missing YAML frontmatter` | File lacks opening/closing `---` | Add standard YAML block at line 1. |
| `frontmatter id does not match filename` | `id: foo` but file is `bar.md` | Rename file to `foo.md` or set `id: bar`. |
| `Broken link '...'` | Target markdown file was moved or deleted | Update the link target path relative to the file. |
| `Orphan document` | File exists in `wiki/` but is not linked anywhere | Add `- [Title](./filename.md)` into `wiki/README.md`. |

---

## 6. Extending with Custom Modern Skills

To add a new specialized capability for AI agents in this repository, follow the Modern Skill package structure under `.agent/skills/`:

```
.agent/skills/<skill_name>/
├── SKILL.md                  # Main orchestration contract
├── scripts/                  # (Optional) Deterministic scripts for calculations/checks
└── references/               # (Optional) Deep reference docs loaded selectively
```

### Steps to create a new skill:
1. **Create Directory:** `.agent/skills/<skill_name>/`.
2. **Author `SKILL.md`:** Prepend YAML frontmatter with `name` and a routing-optimized `description` starting with `"Use this skill when..."` (3rd person) so assistants can discover it semantically without full prompt loading.
3. **Keep it Lean:** Keep `SKILL.md` under 200 lines as the orchestrator. Offload complex schemas or cheat sheets to `references/`.
