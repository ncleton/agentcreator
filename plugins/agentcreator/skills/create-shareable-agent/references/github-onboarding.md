# GitHub onboarding

## Quiet diagnosis

Run `python3 ../../scripts/agentctl.py github-doctor --root "<folder>" --json`. Do not expose technical detail when the environment is ready.

Check Git, GitHub CLI, active authentication, repository-local identity, token-free remote URLs, and the privacy guard. With `--repair`, repair only low-risk configuration.

If several GitHub accounts are authenticated, never infer the owner from a person's name. Match an explicitly provided account exactly. If ownership is not explicit and the choice would change the destination, ask one short question before repository creation.

## First connection

If GitHub CLI is missing, install the official package for the operating system. If no account is connected, explain in one sentence that the connection backs up and updates the agent, open GitHub in the Codex browser when available, then run `gh auth login --web` and `gh auth setup-git`.

The user handles account creation, CAPTCHA, multi-factor authentication, and browser authorization. Never ask the user to paste a token into chat.

## Daily use

- Synchronize only with fast-forward operations.
- Protect unpublished work; never automatically stash, reset, or rebase it.
- Stage only explicit paths through `agentctl.py safe-commit`.
- Verify the remote commit after pushing.
- If authentication expires, ask only for reconnection and open the relevant page.

Never use `gh auth token`, `--show-token`, a credential-bearing URL, or a repository secret file.
