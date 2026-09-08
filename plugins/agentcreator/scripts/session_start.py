#!/usr/bin/env python3
"""Quiet SessionStart maintenance for local Codex installations."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


CHECK_INTERVAL_SECONDS = 24 * 60 * 60


def run(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
        timeout=25,
    )


def refresh_agent_guard(plugin_root: Path, cwd: Path) -> None:
    current = cwd.resolve()
    candidates = [current, *current.parents]
    root = next((path for path in candidates if (path / ".shareable-agent" / "policy.json").is_file()), None)
    if root is None:
        return
    script = plugin_root / "scripts" / "agentctl.py"
    if script.is_file():
        run([sys.executable, str(script), "protect", "--root", str(root)])


def refresh_local_plugin(plugin_data: Path) -> None:
    codex = shutil.which("codex")
    if not codex:
        return
    stamp = plugin_data / "last-update-check"
    now = time.time()
    try:
        if stamp.exists() and now - stamp.stat().st_mtime < CHECK_INTERVAL_SECONDS:
            return
    except OSError:
        pass
    plugin_data.mkdir(parents=True, exist_ok=True)
    result = run([codex, "plugin", "marketplace", "upgrade", "agentcreator"])
    if result.returncode == 0:
        run([codex, "plugin", "add", "agentcreator@agentcreator"])
    stamp.touch(exist_ok=True)


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        event = {}
    plugin_root = Path(os.environ.get("PLUGIN_ROOT", Path(__file__).resolve().parents[1]))
    plugin_data = Path(os.environ.get("PLUGIN_DATA", Path.home() / ".local" / "share" / "agentcreator-plugin"))
    cwd = Path(event.get("cwd") or os.getcwd())
    try:
        refresh_agent_guard(plugin_root, cwd)
        refresh_local_plugin(plugin_data)
    except (OSError, subprocess.SubprocessError):
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
