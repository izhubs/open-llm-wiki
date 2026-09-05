---
name: doc_qc
description: Audit wiki health, verify link integrity, validate YAML frontmatter, and clean up orphan documents.
---

# Document Quality Control Skill (`doc_qc`)

Use this skill to audit and maintain the structural health of the knowledge base.

---

## Audit Checklist

1. **Automated Linter Run:**
   Execute the built-in linter:
   ```bash
   python scripts/check_docs.py
   ```

2. **Remediation Protocols:**
   - **Broken Links:** Locate broken relative paths and update them to point to existing target files.
   - **Orphan Documents:** Every document under `wiki/` must be accessible from `wiki/README.md`. If a document is unlinked, add it to the corresponding section in `wiki/README.md`.
   - **Frontmatter Violations:** Fix missing `id`, `title`, `type`, or `status` fields. Ensure the `id` exactly matches the markdown filename (excluding `.md`).
   - **Status Updates:** When a draft document has been validated and confirmed, update `status: draft` to `status: verified`.

3. **Final Pass:**
   Re-run `python scripts/check_docs.py` to ensure all checks return 0 errors.
