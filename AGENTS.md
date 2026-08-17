# AGENTS.md

## Stack

- **Language**: Python 3.13
- **Testing**: pytest (install with `pip install pytest` if missing; binary lands in `~/.local/bin`)
- **Dependencies**: stdlib only

## Layout

```
truncate_words.py          # sole library module
tests/
└── test_truncate_words.py # pytest suite (15 tests)
specs/001-truncate-words/  # speckit artifacts
.specify/                  # speckit harness scripts + templates
```

## verify_cmd

```bash
python -m pytest tests/ -v
```

Run from repo root. Covers: no-truncation, truncation, whitespace normalization, non-positive max_words.

## Quirks

- `pytest` binary is installed into `~/.local/bin` (not on PATH by default in this environment). Use `python -m pytest` instead of bare `pytest`.
- Ellipsis character is U+2026 `…` (single char), not three dots `...`.
