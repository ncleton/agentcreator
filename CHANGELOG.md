# Changelog

All notable changes to Agent Creator are documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-09-08

### Added

- Distribution guidance that distinguishes a private collaborative project from an installable plugin.
- Required disclosure for plugin context, shared updates, GitHub source rights, workspace roles, and separate service authorization.
- Automatic stable-channel updates as the default for every shared plugin created by Agent Creator, with an explicit manual pinned-version mode.

### Changed

- Shared-agent requests now trigger one distribution question when project versus plugin intent is ambiguous.
- Cross-project installation, centrally managed updates, enterprise role assignment, and bundled connectors now route to plugin creation.
- Generated shared plugins now document workspace branch synchronization and include a quiet daily local update check when the runtime supports hooks.

## [0.2.1] - 2026-09-08

### Changed

- Updated GitHub Actions to their current major releases while retaining immutable full-SHA pins.
- Updated the generated privacy workflow to use the same reviewed checkout release.

## [0.2.0] - 2026-09-08

### Added

- Automatic `create-github-project` skill for production-grade GitHub repositories.
- Repository governance, security, contribution, support, and issue templates.
- Repository-standard validation and hardened GitHub Actions configuration.

### Changed

- Renamed the plugin to `agentcreator` and translated all public-facing content to English.
- Renamed the creation and audit skills to `create-shareable-agent` and `audit-agent`.

## [0.1.0] - 2026-09-08

### Added

- Shareable-agent creation and audit workflows.
- Local private-data boundary, external Git guards, and privacy CI.
- Public marketplace distribution and daily update checks.

[0.2.1]: https://github.com/ncleton/agentcreator/compare/v0.2.0...v0.2.1
[0.3.0]: https://github.com/ncleton/agentcreator/compare/v0.2.1...v0.3.0
[0.2.0]: https://github.com/ncleton/agentcreator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/ncleton/agentcreator/releases/tag/v0.1.0
