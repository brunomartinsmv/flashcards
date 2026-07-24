# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-07-24

### Added

- Domain vocabulary and relationships in `CONTEXT.md` (Language, Fluency, Production, Lote, Inventory Gate, Review Gate, Prompt Import, and related terms).
- Architecture Decision Records under `docs/adr/`:
  - `0001` Process Skill + Language Profiles
  - `0002` Cloze as the default note type
  - `0003` Inventory Gate, Review Gate, and Prompt Import
- Shared process skill `skills/language-anki-flashcards/` with Language Profiles for Spanish and English and `scripts/validate_flashcards.py`.
- Language Folders under `flashcards/spanish/` and `flashcards/english/`.
- Spanish weekly **Lotes** (May–June 2026 Basic batches and the 2026-07-24 Cloze / Basic transition pair).
- `.gitignore` for local junk and Python bytecode.

### Changed

- README rewritten around the personal language → Anki workshop (inventory, Cloze format, validation, import policy) instead of the generic prompt toolkit.
- Legacy generic prompts, banking example, and spaced-repetition reference material moved under `archive/`.

### Deprecated

- Basic/`_____` note type for new **Lotes** (kept only as legacy; Cloze is the default going forward).

## [0.1.0] - 2026-02-19

### Added

- Initial repository: README on spaced repetition (spacing effect, testing effect, Leitner).
- Generic Anki generation prompts (complete, short, and web).
- Banking services example (notes + TSV output).
- Assets for the forgetting curve and Leitner system.
- Local copies of spaced-repetition reference sources.
- MIT `LICENSE` and GitHub repository settings for description/topics.

### Fixed

- Portuguese spelling and diacritics in the README.

[Unreleased]: https://github.com/brunomartinsmv/flashcards/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/brunomartinsmv/flashcards/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/brunomartinsmv/flashcards/releases/tag/v0.1.0
