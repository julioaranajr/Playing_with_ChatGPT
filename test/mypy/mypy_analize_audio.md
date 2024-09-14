# MYPY - Module to analyze audio input using OpenAI's ChatGPT API and play the response using pyttsx3."

## Test the module `analyze_audio.py` using `mypy`

```text

❯ mypy analyze_audio.py

- analyze_audio.py:13: error: Skipping analyzing "pyttsx3":
  module is installed, but missing library stubs or py.typed marker [import-untyped]
- analyze_audio.py:15: error: Skipping analyzing "scipy.io.wavfile":
  module is installed, but missing library stubs or py.typed marker [import-untyped]
- analyze_audio.py:15: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- analyze_audio.py:17: error: Cannot find implementation or
  library stub for module named "sounddevice" [import-not-found]
- analyze_audio.py:19: error: Skipping analyzing "stringcolor":
  module is installed, but missing library stubs or py.typed marker [import-untyped]
  Found 4 errors in 1 file (checked 1 source file)
```

**Note:** The error is due to the fact that the modules `pyttsx3`, `scipy.io.wavfile`, `sounddevice` and `stringcolor` are not typed.

- [See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)

## Dependencies

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [scipy.io.wavfile](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.html)
- [sounddevice](https://pypi.org/project/sounddevice/)
- [stringcolor](https://pypi.org/project/stringcolor/)

## How to install the dependencies

```bash
pip install pyttsx3 scipy sounddevice stringcolor
```

### How to create a package requirements file

```bash
pip freeze > requirements.txt
```

### How to install the dependencies using a requirements file

```bash
pip install -r requirements.txt
```
