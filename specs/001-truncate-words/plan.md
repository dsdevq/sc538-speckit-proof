# Implementation Plan: truncate_words Utility

**Branch**: `001-truncate-words` | **Date**: 2026-08-16 | **Spec**: spec.md

## Summary

Implement a pure-Python `truncate_words(text, max_words)` function that splits on whitespace, joins with single spaces, and appends `…` when truncation occurs. `max_words <= 0` returns `""`.

## Technical Context

**Language/Version**: Python 3.x (no version-specific features used)

**Primary Dependencies**: stdlib only (`str.split`)

**Storage**: N/A

**Testing**: pytest

**Target Platform**: Any

**Project Type**: library (single module)

**Performance Goals**: N/A — utility function, negligible overhead

**Constraints**: No external dependencies

**Scale/Scope**: Single function

## Project Structure

```text
truncate_words.py        # implementation
tests/
└── test_truncate_words.py
```

**Structure Decision**: Flat layout — one module, one test file. No package overhead needed for a single utility function.
