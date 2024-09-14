# MYPY Report - chatbot.py

## Test the module `chatbot.py` using `mypy`

```bash
❯ mypy chatbot.py
chatbot.py:45: error: Skipping analyzing "pyttsx3": module is installed, but missing library stubs or py.typed marker  [import-untyped]
chatbot.py:45: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
chatbot.py:47: error: Skipping analyzing "stringcolor": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 2 errors in 1 file (checked 1 source file)
```

**Note:** The error is due to the fact that the modules `pyttsx3` and `stringcolor` are not typed.

- [See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)

## Dependencies

- [pyttsx3](https://pypi.org/project/pyttsx3/)

- [stringcolor](https://pypi.org/project/stringcolor/)

## How to install the dependencies

```bash
pip install pyttsx3 stringcolor
```
