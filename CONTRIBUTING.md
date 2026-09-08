# Contributing

Thank you for improving Agent Creator. Contributions must preserve the privacy boundary and remain useful across macOS, Linux, and Windows.

## Development workflow

1. Fork or clone the repository and create a focused branch from `main`.
2. Keep customer, company, and personal data out of every file, test, issue, branch name, commit, and pull request.
3. Make the smallest coherent change and add behavior-focused tests.
4. Run `make validate`.
5. Open a pull request using the repository template.

Direct pushes, force pushes, and branch deletion are blocked on `main`. Pull requests must pass the required `validate` check.

## Skill changes

Keep skill descriptions concise and explicit about when they should activate. Put conditional detail in references and keep implicit invocation enabled unless explicit-only behavior is required.

## Commit and pull request quality

Use imperative commit subjects. Explain the user-visible outcome, privacy impact, compatibility impact, and verification performed in the pull request.

By contributing, you agree that your contribution is licensed under the MIT License.
