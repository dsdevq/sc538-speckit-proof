# Tasks: Slugify Utility

**Input**: Design documents from `/specs/001-slugify-utility/`

**Prerequisites**: plan.md, spec.md

## Phase 1: Setup

- [x] T001 Create feature directory and speckit artifacts in `specs/001-slugify-utility/`

---

## Phase 2: User Story 1 - Slugify Text for URL Use (Priority: P1)

**Goal**: Implement `slugify(text)` in `slugify.py` with full test coverage.

**Independent Test**: `python -m pytest tests/test_slugify.py`

### Tests for User Story 1

- [x] T002 [P] [US1] Write pytest suite in `tests/test_slugify.py` covering: ASCII, unicode/accents, punctuation, empty string, repeated hyphens, idempotency, all-punctuation input

### Implementation for User Story 1

- [x] T003 [US1] Implement `slugify(text: str) -> str` in `slugify.py` using `unicodedata` + `re`

---

## Phase 3: Infrastructure

- [x] T004 Create `AGENTS.md` documenting repo layout, test command, and gotchas
- [x] T005 Create `PLAN.md` with destination, decisions, and completed tasks

---

## Dependencies & Execution Order

- T001 → T002 (tests written) → T003 (implementation) → all tests pass
- T004, T005 independent of T002/T003
