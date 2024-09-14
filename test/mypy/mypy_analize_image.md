# MYPY - Module to analyze an image using OpenAI's GPT-4 model

## Test the module `analyze_image.py` using `mypy`

```bash
❯ mypy analyze_image.py
analyze_image.py:11: error: Skipping analyzing "stringcolor": module is installed, but missing library stubs or py.typed marker  [import-untyped]
analyze_image.py:11: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
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

### How to create a package requirements file

```bash
pip freeze > requirements.txt
```

### How to install the dependencies using a requirements file

```bash
pip install -r requirements.txt
```
