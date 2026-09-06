---
name: doc_ingest
description: Use this skill when the user provides raw text, notes, transcripts, or asks to compile unstructured ideas into structured wiki documents with YAML frontmatter.
---

# Document Ingestion Skill (`doc_ingest`)

Use this skill when the user provides raw text, notes, conversation logs, or requirements and wants to convert them into permanent knowledge documents.

---

## Workflow Steps

### 1. Classification & ID Generation
- Determine the document type:
  - `sop`: Step-by-step repeatable operational procedures.
  - `concept`: Domain models, definitions, and mental models.
  - `decision`: Architecture or policy decisions (with rationale and trade-offs).
  - `research`: In-depth analysis, benchmark comparisons, or external notes.
- Select a clean lowercase slug for the ID (e.g., `git_sync_flow`).

### 2. Format with YAML Frontmatter
Every ingested document must begin with:

```markdown
---
id: <document_id>
title: <Clear Human-Readable Title>
type: <concept|sop|decision|research>
status: draft
tags: [<relevant>, <search>, <tags>]
last_updated: <YYYY-MM-DD>
---
```

### 3. File Creation
- Save the file to `wiki/<document_id>.md`.
- Ensure clean Markdown structure (headings starting at `#`, bullet points, code blocks).
- Avoid fluff, pleasantries, and unnecessary conversational fillers.

### 4. Index Registration
- Add an entry for the new document inside `wiki/README.md` under the appropriate category section.
- Use relative Markdown link syntax: `- [filename.md](./filename.md): Brief description`.

### 5. Verification
- Run the document integrity check:
  ```bash
  python scripts/check_docs.py
  ```
- Ensure exit code is 0 before reporting completion to the user.
