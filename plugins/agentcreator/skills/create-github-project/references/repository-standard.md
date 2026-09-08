# Repository standard

Apply the standard proportionally to the project, but do not omit required controls merely because the repository is small.

## Required repository content

- A concise `README.md` covering purpose, capabilities, installation, usage, security, support, and maintenance.
- A technology-appropriate `.gitignore`, `.gitattributes`, and `.editorconfig`.
- `LICENSE` only after the owner has selected the intended legal grant.
- `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, and `CHANGELOG.md` for shared or public projects.
- `CODE_OF_CONDUCT.md` when outside contribution is accepted.
- `CODEOWNERS`, a pull request template, structured bug and feature issue forms, and disabled blank issues.
- `AGENTS.md` with repository-specific validation, safety, and maintenance invariants when Codex will maintain the project.

## Automated quality

- Provide one canonical local validation command and run it in CI.
- Test supported runtime versions when compatibility claims span several versions.
- Grant workflows minimum explicit `permissions`.
- Pin third-party GitHub Actions to full commit SHAs and retain the release tag in a comment for maintainability.
- Add Dependabot for ecosystems actually used, including GitHub Actions.
- Block obvious secrets and inspect tracked and historical files before the first public push.

## GitHub settings

- Set a useful description, homepage when relevant, and focused topics.
- Enable issues only when the project provides support or accepts feedback.
- Prefer squash merge, delete merged branches automatically, and disable unused merge strategies.
- Protect the default branch: require pull requests, strict required status checks, conversation resolution, linear history, and blocked force pushes and deletions.
- Enable vulnerability alerts, security updates, secret scanning, push protection, and private vulnerability reporting when the plan and repository visibility support them.
- Create labels needed by issue forms and automation before those forms are used.

## Releases and verification

- Use semantic versions for distributable software and maintain a changelog.
- Tag the exact merged commit and create release notes that link changes and migration requirements.
- Verify a clean install or checkout from the canonical remote, not only the working tree.
- Query the GitHub community profile and record any intentional gap.
