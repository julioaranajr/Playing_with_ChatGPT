# MYPY Report - generate_text.py

## Test the module `generate_text.py` using `mypy`

```bash
❯ mypy generate_text.py
generate_text.py:28: error: Skipping analyzing "pyttsx3": module is installed, but missing library stubs or py.typed marker  [import-untyped]
generate_text.py:28: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)
```

**Note:** The error is due to the fact that the module `pyttsx3` is not typed.

- [See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)

## Dependencies

- [pyttsx3](https://pypi.org/project/pyttsx3/)

## How to install the dependencies

```bash
pip install pyttsx3
```
