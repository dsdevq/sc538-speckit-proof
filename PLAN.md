# PLAN.md

## Destination

A `slugify(text: str) -> str` Python function in `slugify.py`, with a pytest suite in `tests/test_slugify.py` covering unicode, punctuation, and empty string. PR references "Closes #2".

## Decisions so far

- **stdlib only** — `unicodedata` + `re`; no third-party slug libraries (keeps dep count zero).
- **NFD normalization** to decompose accented chars, then drop combining-category codepoints — standard approach, correct for all Latin-script accents.
- **Module at repo root** (`slugify.py`) — no `src/` nesting needed for a single-function utility.
- **Tests in `tests/test_slugify.py`** — conventional pytest layout.

## Milestones

- [x] M1: speckit feature scaffold created (`specs/001-slugify-utility/`)
- [x] M2: `slugify.py` implemented and all 33 tests passing

## Tasks — M2 (complete)

- [x] T001 Create speckit feature directory via `create-new-feature.sh`
- [x] T002 Write `specs/001-slugify-utility/spec.md`
- [x] T003 Write `specs/001-slugify-utility/plan.md`
- [x] T004 Write `specs/001-slugify-utility/tasks.md`
- [x] T005 Implement `slugify.py`
- [x] T006 Write `tests/test_slugify.py` (33 tests: ASCII, unicode, punctuation, hyphens, edge cases)
- [x] T007 Run `python -m pytest` — all 33 pass
- [x] T008 Write `AGENTS.md` and `PLAN.md`
- [x] T009 Commit

## Out of scope

- CLI wrapper for `slugify`
- PyPI packaging
- Non-ASCII output characters (non-Latin scripts map to empty — acceptable per spec)
