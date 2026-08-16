# Feature Specification: truncate_words Utility

**Feature Branch**: `001-truncate-words`

**Created**: 2026-08-16

**Status**: Complete

**Input**: User description: "truncate_words utility for text word truncation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Word Truncation Utility (Priority: P1)

A developer calls `truncate_words(text, max_words)` to limit long text to a fixed number of words, normalizing any irregular whitespace and appending an ellipsis when the text was truncated.

**Why this priority**: This is the sole deliverable — everything else is acceptance criteria for this one function.

**Independent Test**: Import `truncate_words` and call it with various inputs; verify return values.

**Acceptance Scenarios**:

1. **Given** text shorter than max_words words, **When** called, **Then** returns all words joined by single spaces (no ellipsis).
2. **Given** text longer than max_words words, **When** called, **Then** returns first max_words words joined by single spaces with `…` appended.
3. **Given** text with extra/leading/trailing whitespace, **When** called, **Then** normalizes to single spaces.
4. **Given** max_words <= 0, **When** called, **Then** returns empty string `""`.

---

### Edge Cases

- Empty string input → returns `""`.
- max_words exactly equals word count → no ellipsis.
- Multiple consecutive spaces between words → collapsed to single space.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `truncate_words(text, max_words)` MUST split text on any whitespace.
- **FR-002**: Words MUST be joined by single spaces in the output.
- **FR-003**: When `len(words) > max_words`, MUST append `…` (U+2026) to output.
- **FR-004**: When `max_words <= 0`, MUST return `""`.
- **FR-005**: When `len(words) <= max_words`, MUST return all words with no ellipsis.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pytest` test suite passes with zero failures covering all four acceptance scenarios.

## Assumptions

- Pure Python utility, no external dependencies.
- Text encoding is UTF-8; ellipsis is the single Unicode character U+2026 (`…`).
