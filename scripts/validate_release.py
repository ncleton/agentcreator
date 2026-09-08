#!/usr/bin/env python3
"""Dependency-free validation for the public marketplace repository."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "agentcreator"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    manifest = load_json(manifest_path)
    marketplace = load_json(marketplace_path)

    if manifest.get("name") != "agentcreator":
        errors.append("plugin name must be agentcreator")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", str(manifest.get("version", ""))):
        errors.append("plugin version must be semantic")
    if manifest.get("skills") != "./skills/":
        errors.append("plugin must expose ./skills/")
    entries = [item for item in marketplace.get("plugins", []) if item.get("name") == "agentcreator"]
    if len(entries) != 1:
        errors.append("marketplace must contain one agentcreator entry")
    elif entries[0].get("source", {}).get("path") != "./plugins/agentcreator":
        errors.append("marketplace plugin path is invalid")

    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHANGELOG.md",
        ROOT / "CODE_OF_CONDUCT.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "GOVERNANCE.md",
        ROOT / "SECURITY.md",
        ROOT / "SUPPORT.md",
        ROOT / ".editorconfig",
        ROOT / ".gitattributes",
        ROOT / ".github" / "CODEOWNERS",
        ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml",
        ROOT / ".github" / "dependabot.yml",
        ROOT / "docs" / "privacy.md",
        PLUGIN / "skills" / "create-shareable-agent" / "SKILL.md",
        PLUGIN / "skills" / "audit-agent" / "SKILL.md",
        PLUGIN / "skills" / "create-github-project" / "SKILL.md",
        PLUGIN / "scripts" / "agentctl.py",
        PLUGIN / "scripts" / "session_start.py",
        PLUGIN / "hooks" / "hooks.json",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"missing {path.relative_to(ROOT)}")

    for path in PLUGIN.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "[TODO:" in text:
            errors.append(f"unfinished placeholder in {path.relative_to(ROOT)}")

    hooks = load_json(PLUGIN / "hooks" / "hooks.json")
    if "SessionStart" not in hooks.get("hooks", {}):
        errors.append("SessionStart maintenance hook is missing")

    legacy_paths = [ROOT / "plugins" / "createur-agents"]
    for path in legacy_paths:
        if path.exists():
            errors.append(f"legacy path still exists: {path.relative_to(ROOT)}")

    workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
    if "permissions:\n  contents: read" not in workflow:
        errors.append("validation workflow permissions must be read-only")
    if "actions/checkout@v" in workflow or "actions/setup-python@v" in workflow:
        errors.append("GitHub Actions must be pinned to full commit SHAs")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Release valid: agentcreator {manifest['version']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
