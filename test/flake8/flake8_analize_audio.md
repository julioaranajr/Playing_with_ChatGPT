# Flake8 - Module to analyze audio input using OpenAI's ChatGPT API and play the response using pyttsx3

## 1st.Run

```bash
❯ flake8 analyze_audio.py
analyze_audio.py:24:25: Q000 Double quotes found but single quotes preferred
analyze_audio.py:35:1: D107 Missing docstring in __init__
analyze_audio.py:35:43: Q000 Double quotes found but single quotes preferred
analyze_audio.py:41:1: D200 One-line docstring should fit on one line with quotes
analyze_audio.py:42:80: E501 line too long (84 > 79 characters)
analyze_audio.py:45:16: Q000 Double quotes found but single quotes preferred
analyze_audio.py:45:80: E501 line too long (87 > 79 characters)
analyze_audio.py:45:81: Q000 Double quotes found but single quotes preferred
analyze_audio.py:51:1: D200 One-line docstring should fit on one line with quotes
analyze_audio.py:51:1: D401 First line should be in imperative mood; try rephrasing
analyze_audio.py:60:74: Q000 Double quotes found but single quotes preferred
analyze_audio.py:60:80: E501 line too long (80 > 79 characters)
analyze_audio.py:65:18: Q000 Double quotes found but single quotes preferred
analyze_audio.py:65:40: Q000 Double quotes found but single quotes preferred
analyze_audio.py:69:1: D200 One-line docstring should fit on one line with quotes
analyze_audio.py:73:34: Q000 Double quotes found but single quotes preferred
analyze_audio.py:79:1: D205 1 blank line required between summary line and description
analyze_audio.py:79:1: D400 First line should end with a period
analyze_audio.py:83:36: Q000 Double quotes found but single quotes preferred
analyze_audio.py:90:1: D200 One-line docstring should fit on one line with quotes
analyze_audio.py:97:16: Q000 Double quotes found but single quotes preferred
analyze_audio.py:102:11: Q000 Double quotes found but single quotes preferred
```

-Q000: Double quotes found but single quotes preferred
-D107: Missing docstring in **init**
-D200: One-line docstring should fit on one line with quotes
-E501: line too long (Bigger than 79 characters)
-D401: First line should be in imperative mood; try rephrasing
-D205: 1 blank line required between summary line and description
-D400: First line should end with a period

After fixing the issues,now the code is clean and ready to be used.
