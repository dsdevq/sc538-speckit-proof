# AGENTS.md

## Project

`sc538-speckit-proof` — scratch repo for devclaw speckit shakedown.

## Stack

- **Language**: Python 3.8+ (tested on 3.13)
- **Testing**: pytest (stdlib only for production code; `pip install pytest` required in fresh envs)
- **Dependencies**: none (slugify uses only `unicodedata` + `re`)

## Layout

```
slugify.py                    # slugify() implementation
tests/
└── test_slugify.py           # pytest suite (33 tests)
specs/
└── 001-slugify-utility/      # speckit feature artifacts
    ├── spec.md
    ├── plan.md
    └── tasks.md
.specify/                     # speckit harness (scripts, templates, workflows)
```

## Test / Verify

```bash
pip install pytest            # if not already installed
python -m pytest              # runs all tests
python -m pytest -v           # verbose output
```

**verify_cmd**: `python -m pytest`

## Gotchas

- `pytest` binary may not be on PATH after pip install in some envs; use `python -m pytest` instead.
- No `pyproject.toml` / `setup.py` — `slugify.py` is importable directly from the repo root.
- `.specify/` is the speckit harness; do not delete it.
