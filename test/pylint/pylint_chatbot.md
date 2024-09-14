# Pylint Report - Module ChatBot

## Module ChatBot using OpenAI's ChatGPT API

```bash
❯ pylint chatbot.py
************* Module chatbot
chatbot.py:9:0: W0401: Wildcard import stringcolor (wildcard-import)
chatbot.py:9:0: W0614: Unused import(s) main, name, bold and underline from wildcard import of stringcolor (unused-wildcard-import)

-----------------------------------
Your code has been rated at 9.80/10
```

- W0401: Wildcard import stringcolor (wildcard-import)
- W0614: Unused import(s) main, name, bold and underline from wildcard import of stringcolor (unused-wildcard-import)

After fixing the code, the rating improved to 10.00/10.

```bash
❯ pylint chatbot.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.80/10, +0.20)
```
