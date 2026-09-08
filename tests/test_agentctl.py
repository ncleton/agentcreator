from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
SCRIPT = REPOSITORY / "plugins" / "createur-agents" / "scripts" / "agentctl.py"


class AgentCtlTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.root = self.base / "agent-test"
        self.runtime = self.base / "runtime"
        self.env = dict(os.environ, CREATEUR_AGENTS_HOME=str(self.runtime))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def call(self, *args: str, ok: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            text=True,
            capture_output=True,
            env=self.env,
            check=False,
        )
        if ok and result.returncode != 0:
            self.fail(f"command failed ({result.returncode})\nstdout={result.stdout}\nstderr={result.stderr}")
        return result

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=True,
        )

    def create_agent(self) -> None:
        result = self.call(
            "create",
            "--root",
            str(self.root),
            "--description",
            "Classer des factures et préparer leur suivi.",
            "--json",
        )
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])

    def configure_identity(self) -> None:
        self.git("config", "user.name", "Test User")
        self.git("config", "user.email", "test@example.com")

    def commit_initial_agent(self) -> None:
        self.configure_identity()
        listed = self.git("ls-files", "--others", "--exclude-standard", "-z").stdout
        paths = [item for item in listed.split("\0") if item]
        self.assertTrue(paths)
        self.call(
            "safe-commit",
            "--root",
            str(self.root),
            "--message",
            "Initial agent",
            "--paths",
            *paths,
        )

    def test_create_installs_external_privacy_boundary(self) -> None:
        self.create_agent()
        self.assertTrue((self.root / "AGENTS.md").exists())
        self.assertTrue((self.root / ".agent-private").is_symlink())
        self.assertFalse(str((self.root / ".agent-private").resolve()).startswith(str(self.root)))
        hook_path = self.git("config", "--local", "--get", "core.hooksPath").stdout.strip()
        self.assertTrue(hook_path)
        self.assertFalse(Path(hook_path).resolve().is_relative_to(self.root.resolve()))
        self.assertTrue((Path(hook_path) / "pre-commit").exists())
        self.assertTrue((Path(hook_path) / "pre-push").exists())

    def test_guard_rejects_ignored_file_forced_into_index(self) -> None:
        self.create_agent()
        self.commit_initial_agent()
        private_file = self.root / ".env"
        private_file.write_text("SERVICE_PASSWORD=not-a-real-password-value\n", encoding="utf-8")
        self.git("add", "-f", ".env")
        result = self.call("guard", "--root", str(self.root), "--staged", "--json", ok=False)
        self.assertEqual(result.returncode, 2)
        codes = {item["code"] for item in json.loads(result.stdout)["findings"]}
        self.assertIn("ignored-file-is-tracked", codes)
        self.assertIn("environment-file", codes)

    def test_guard_rejects_personal_data_in_agents_file(self) -> None:
        self.create_agent()
        self.commit_initial_agent()
        with (self.root / "AGENTS.md").open("a", encoding="utf-8") as handle:
            handle.write("\nContact interne: personne@example.fr\n")
        self.git("add", "AGENTS.md")
        result = self.call("guard", "--root", str(self.root), "--staged", "--json", ok=False)
        self.assertEqual(result.returncode, 2)
        codes = {item["code"] for item in json.loads(result.stdout)["findings"]}
        self.assertIn("email", codes)

    def test_repair_is_additive_and_idempotent(self) -> None:
        self.root.mkdir()
        original = "# Agent existant\n\nRègle métier conservée.\n"
        (self.root / "AGENTS.md").write_text(original, encoding="utf-8")
        self.call("repair", "--root", str(self.root), "--mode", "collaborative")
        self.call("repair", "--root", str(self.root), "--mode", "collaborative")
        updated = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(original.strip(), updated)
        self.assertEqual(updated.count("BEGIN CREATEUR-AGENTS PRIVACY"), 1)
        policy = json.loads((self.root / ".shareable-agent" / "policy.json").read_text(encoding="utf-8"))
        self.assertEqual(policy["mode"], "collaborative")

    def test_external_hook_blocks_commit(self) -> None:
        self.create_agent()
        self.commit_initial_agent()
        (self.root / ".env").write_text("PRIVATE_VALUE=blocked-example-value\n", encoding="utf-8")
        self.git("add", "-f", ".env")
        result = subprocess.run(
            ["git", "commit", "-m", "Must be blocked"],
            cwd=self.root,
            text=True,
            capture_output=True,
            env=self.env,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Publication bloquée", result.stdout + result.stderr)

    def test_history_scan_finds_previous_private_file(self) -> None:
        self.create_agent()
        self.commit_initial_agent()
        private_file = self.root / "clients" / "archive.csv"
        private_file.parent.mkdir()
        private_file.write_text("nom,email\nExemple,personne@example.fr\n", encoding="utf-8")
        self.git("add", "-f", "clients/archive.csv")
        subprocess.run(
            ["git", "commit", "--no-verify", "-m", "Unsafe historical commit"],
            cwd=self.root,
            text=True,
            capture_output=True,
            env=self.env,
            check=True,
        )
        self.call("repair", "--root", str(self.root), ok=False)
        result = self.call("audit", "--root", str(self.root), "--history", "--json", ok=False)
        payload = json.loads(result.stdout)
        codes = {item["code"] for item in payload["findings"]}
        self.assertTrue(any(code.startswith("history-") for code in codes))


if __name__ == "__main__":
    unittest.main()
