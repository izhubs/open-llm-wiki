---
id: sample_sop
title: Sample Standard Operating Procedure
type: sop
status: verified
tags: [template, sop, guide]
last_updated: 2026-09-05
---

# Sample Standard Operating Procedure

This document provides a reference implementation of a standard operating procedure (SOP) within the Open LLM-Wiki architecture.

---

## 1. Purpose

Define the repeatable steps required to ingest raw text, transcripts, or meeting notes into a structured Wiki document.

---

## 2. Prerequisites

- A running AI coding assistant or CLI session in the repository.
- Raw text or source material to be ingested.

---

## 3. Execution Steps

1. **Clean the source material:** Remove duplicated headers, conversation filler, and irrelevant metadata.
2. **Assign metadata:**
   - Choose a unique slug for `id` (e.g., `git_branching_guide`).
   - Define appropriate `type` (`sop`, `concept`, `decision`, or `research`).
   - Add searchable tags.
3. **Write the file:** Save to `wiki/<id>.md` using standard Markdown headings.
4. **Register in Index:** Add a link to the new file in [wiki/README.md](./README.md).
5. **Run Verification:**
   ```bash
   python scripts/check_docs.py
   ```
   Confirm that zero errors are reported.
