---
name: create-github-project
description: Create, initialize, publish, or upgrade a GitHub repository to production-grade standards. Use when the user asks to create a GitHub project or repository, publish a folder on GitHub, initialize Git or GitHub, or make a repository exemplary. Do not use for routine commits to an already governed repository.
---

# Create an exemplary GitHub project

Create or upgrade the repository with complete documentation, privacy safeguards, automated validation, secure settings, and a maintainable contribution workflow. Keep interaction short: infer sensible technical defaults and ask one concise question only when ownership, visibility, or licensing cannot be established safely.

## Workflow

1. Inspect the folder, existing Git state, instructions, tests, package metadata, and uncommitted work. Preserve all existing user changes.
2. Establish the exact GitHub owner and repository name. Never infer a username from a person's name. When several accounts are authenticated, match the explicitly requested owner and verify the active API identity before creation.
3. Default new repositories to private. Public visibility requires an explicit user request. Never change existing visibility without explicit authorization.
4. Run the Agent Creator privacy audit when available. Do not publish while critical or high privacy findings remain.
5. Read [repository-standard.md](references/repository-standard.md) and apply every relevant required item. Mark genuinely inapplicable items explicitly rather than silently omitting them.
6. Use GitHub CLI for authentication and repository operations. Keep credentials in the operating system credential store; never print tokens or place them in remotes, files, logs, or chat.
7. Create a focused branch and pull request when a protected default branch already exists. Never bypass required checks, reviews, or branch protection.
8. Configure repository metadata, merge behavior, security features, and default-branch protection. Require the exact CI check that has already run successfully.
9. Verify the remote repository, default branch, workflow result, protection settings, community profile, and installation or build path before reporting completion.

## Authorization boundaries

- Do not add a license that grants reuse rights unless the user selected it or the repository already declares the intended license.
- Do not invite collaborators, change visibility, transfer ownership, delete a repository, rewrite history, or weaken protection without explicit authorization.
- Creating the repository and applying standard settings is authorized when the user asks to create or publish the project.

## Completion standard

Report the canonical URL, visibility, default branch, required checks, security status, release/version state, and any owner decision still needed. Avoid claiming the repository is exemplary when a required item is missing or unverified.
