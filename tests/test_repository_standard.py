from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "agentcreator"


class RepositoryStandardTests(unittest.TestCase):
    def test_required_community_and_governance_files_exist(self) -> None:
        required = [
            "README.md",
            "LICENSE",
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "GOVERNANCE.md",
            "SECURITY.md",
            "SUPPORT.md",
            ".editorconfig",
            ".gitattributes",
            ".github/CODEOWNERS",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/feature_request.yml",
            ".github/ISSUE_TEMPLATE/config.yml",
            ".github/dependabot.yml",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_plugin_and_marketplace_use_canonical_identity(self) -> None:
        manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "agentcreator")
        self.assertEqual(manifest["repository"], "https://github.com/ncleton/agentcreator")
        self.assertEqual(marketplace["name"], "agentcreator")
        self.assertEqual(marketplace["plugins"][0]["name"], "agentcreator")
        self.assertEqual(marketplace["plugins"][0]["source"]["path"], "./plugins/agentcreator")

    def test_three_implicit_skills_are_packaged(self) -> None:
        expected = {"audit-agent", "create-github-project", "create-shareable-agent"}
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, expected)
        for name in expected:
            metadata = (PLUGIN / "skills" / name / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn("allow_implicit_invocation: true", metadata)

    def test_workflow_is_minimally_scoped_and_sha_pinned(self) -> None:
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertNotIn("actions/checkout@v", workflow)
        self.assertNotIn("actions/setup-python@v", workflow)


if __name__ == "__main__":
    unittest.main()
