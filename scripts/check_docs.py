#!/usr/bin/env python3
"""
scripts/check_docs.py
Zero-dependency document linter for Open LLM-Wiki.

Checks:
1. YAML frontmatter presence and required fields (id, title, type, status).
2. Filename-to-ID alignment.
3. Relative link integrity within the wiki directory.
4. Orphan document detection (documents not linked in wiki/README.md).

Exit code: 0 if all checks pass, 1 if any check fails.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REQUIRED_FRONTMATTER_FIELDS = ["id", "title", "type", "status"]
VALID_TYPES = {"concept", "sop", "research", "decision"}
VALID_STATUSES = {"draft", "verified", "deprecated"}


def parse_frontmatter(content: str) -> dict[str, str] | None:
    """Extract YAML frontmatter between opening and closing ---."""
    if not content.startswith("---"):
        return None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    
    raw_frontmatter = parts[1]
    result: dict[str, str] = {}
    for line in raw_frontmatter.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            result[key.strip()] = val.strip().strip("\"'")
    return result


def find_markdown_links(content: str) -> list[str]:
    """Find markdown links [text](target) excluding external http(s) links and anchors."""
    # Match [text](target)
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    links = []
    for match in re.finditer(pattern, content):
        target = match.group(2).strip()
        # Exclude web URLs and pure anchor links
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Strip anchor from target if present
        target_path = target.split("#")[0]
        if target_path:
            links.append(target_path)
    return links


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    wiki_dir = repo_root / "wiki"
    
    if not wiki_dir.exists():
        print(f"[ERROR] Wiki directory not found at {wiki_dir}")
        return 1

    wiki_files = sorted(wiki_dir.glob("**/*.md"))
    if not wiki_files:
        print(f"[WARN] No markdown files found in {wiki_dir}")
        return 0

    errors: list[str] = []
    warnings: list[str] = []
    
    # Track references for orphan detection
    referenced_files: set[Path] = set()
    index_file = wiki_dir / "README.md"

    print(f"Checking {len(wiki_files)} document(s) in {wiki_dir.relative_to(repo_root)}...\n")

    for file_path in wiki_files:
        rel_path = file_path.relative_to(repo_root)
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as err:
            errors.append(f"{rel_path}: Failed to read file ({err})")
            continue

        frontmatter = parse_frontmatter(content)
        if frontmatter is None:
            errors.append(f"{rel_path}: Missing YAML frontmatter (must start with '---')")
        else:
            # Check required fields
            for field in REQUIRED_FRONTMATTER_FIELDS:
                if field not in frontmatter:
                    errors.append(f"{rel_path}: Missing required frontmatter field '{field}'")

            # Check ID vs filename
            doc_id = frontmatter.get("id", "")
            expected_id = file_path.stem
            # Allow index for README
            if file_path.name.lower() == "readme.md" and doc_id in ("index", "readme"):
                pass
            elif doc_id and doc_id != expected_id:
                errors.append(f"{rel_path}: frontmatter id '{doc_id}' does not match filename '{expected_id}'")

            # Check type validity
            doc_type = frontmatter.get("type", "")
            if doc_type and doc_type not in VALID_TYPES:
                warnings.append(f"{rel_path}: Non-standard type '{doc_type}' (expected one of: {', '.join(sorted(VALID_TYPES))})")

            # Check status validity
            doc_status = frontmatter.get("status", "")
            if doc_status and doc_status not in VALID_STATUSES:
                warnings.append(f"{rel_path}: Non-standard status '{doc_status}' (expected one of: {', '.join(sorted(VALID_STATUSES))})")

        # Check relative link targets
        links = find_markdown_links(content)
        for link in links:
            # Resolve link relative to the current file's parent directory
            resolved_target = (file_path.parent / link).resolve()
            if not resolved_target.exists():
                errors.append(f"{rel_path}: Broken link '{link}' (target does not exist: {resolved_target.name})")
            else:
                if resolved_target.suffix.lower() == ".md":
                    referenced_files.add(resolved_target)

    # Check for orphan files (not linked in index or any document)
    for file_path in wiki_files:
        if file_path == index_file:
            continue
        if file_path not in referenced_files:
            rel_path = file_path.relative_to(repo_root)
            warnings.append(f"{rel_path}: Orphan document (not linked in wiki/README.md or any other wiki document)")

    # Print results
    if warnings:
        print("[WARNINGS]")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("[ERRORS]")
        for e in errors:
            print(f"  x {e}")
        print(f"\nResult: FAILED ({len(errors)} error(s), {len(warnings)} warning(s))")
        return 1

    print(f"Result: PASSED ({len(wiki_files)} files verified, 0 errors, {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
