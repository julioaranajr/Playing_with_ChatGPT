# MYPY Report - func_completion.py

## Test the module `func_completion.py` using `mypy`

```bash
❯ mypy func_completion.py
func_completion.py:35: error: Skipping analyzing "stringcolor": module is installed, but missing library stubs or py.typed marker  [import-untyped]
func_completion.py:35: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)
```

**Note:** The error is due to the fact that the module `stringcolor` is not typed.

- [See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)

## Dependencies

- [stringcolor](https://pypi.org/project/stringcolor/)

## How to install the dependencies

```bash
pip install stringcolor
```
