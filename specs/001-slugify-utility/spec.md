# Feature Specification: Slugify Utility

**Feature Branch**: `001-slugify-utility`

**Created**: 2026-08-16

**Status**: Approved

**Input**: User description: "a slugify(text) Python utility (lowercase, strip accents, whitespace runs to single hyphen, drop non-alphanumerics, collapse repeated hyphens) with unit tests covering unicode, punctuation, and empty string"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Slugify Text for URL Use (Priority: P1)

A developer calls `slugify(text)` to convert arbitrary human-readable text into a URL-safe slug: lowercase, ASCII-only, words joined by hyphens.

**Why this priority**: Core functionality — everything else depends on it.

**Independent Test**: Import `slugify` from the module, call it with sample strings, assert expected slugs.

**Acceptance Scenarios**:

1. **Given** `"Hello World"`, **When** `slugify("Hello World")`, **Then** returns `"hello-world"`
2. **Given** `"Café naïve"`, **When** `slugify("Café naïve")`, **Then** returns `"cafe-naive"` (accents stripped)
3. **Given** `"hello, world!"`, **When** `slugify("hello, world!")`, **Then** returns `"hello-world"` (punctuation dropped)
4. **Given** `""`, **When** `slugify("")`, **Then** returns `""` (empty string safe)
5. **Given** `"über--cool"`, **When** `slugify("über--cool")`, **Then** returns `"uber-cool"` (repeated hyphens collapsed)

---

### Edge Cases

- Empty string returns empty string (no crash, no leading/trailing hyphens).
- String that is all punctuation/spaces returns empty string.
- Already-slug input is idempotent.
- Multiple consecutive whitespace characters treated as one separator.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `slugify(text)` MUST convert input to lowercase.
- **FR-002**: `slugify(text)` MUST strip Unicode combining characters (accents) via NFD normalization.
- **FR-003**: `slugify(text)` MUST replace any run of whitespace with a single hyphen.
- **FR-004**: `slugify(text)` MUST drop all characters that are not ASCII alphanumeric or hyphen.
- **FR-005**: `slugify(text)` MUST collapse consecutive hyphens into one.
- **FR-006**: `slugify(text)` MUST strip leading and trailing hyphens from the result.
- **FR-007**: `slugify("")` MUST return `""` without raising an exception.

### Key Entities

- **`slugify(text: str) -> str`**: Pure function, no side effects.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `python -m pytest` exits 0 with all tests passing.
- **SC-002**: Tests cover: ASCII text, unicode/accented text, punctuation, empty string, repeated hyphens.

## Assumptions

- Python 3.8+ standard library only (no third-party dependencies).
- Module lives at `slugify.py` in the repository root; tests in `tests/test_slugify.py`.
