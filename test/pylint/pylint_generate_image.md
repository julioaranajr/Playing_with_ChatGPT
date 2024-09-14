# Pylint Report - Module to generate images using OpenAI's DALL-E model

## 1st run

```bash
❯ pylint generate_image.py
************* Module generate_image
generate_image.py:31:0: C0301: Line too long (103/100) (line-too-long)
generate_image.py:1:0: C0114: Missing module docstring (missing-module-docstring)
generate_image.py:5:0: W0401: Wildcard import stringcolor (wildcard-import)
generate_image.py:8:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
generate_image.py:14:0: C0115: Missing class docstring (missing-class-docstring)
generate_image.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
generate_image.py:19:29: W0621: Redefining name 'prompt' from outer scope (line 39) (redefined-outer-name)
generate_image.py:29:25: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)
generate_image.py:14:0: R0903: Too few public methods (1/2) (too-few-public-methods)
generate_image.py:5:0: W0614: Unused import(s) main, name, bold and underline from wildcard import of stringcolor (unused-wildcard-import)

-----------------------------------
Your code has been rated at 6.30/10
```

## 2nd run

```bash
❯ pylint generate_image.py
************* Module generate_image
generate_image.py:44:0: C0301: Line too long (103/100) (line-too-long)
generate_image.py:29:29: W0621: Redefining name 'prompt' from outer scope (line 52) (redefined-outer-name)
generate_image.py:42:25: W3101: Missing timeout argument for method 'requests.get' can cause your program to hang indefinitely (missing-timeout)

------------------------------------------------------------------
Your code has been rated at 8.97/10 (previous run: 6.30/10, +2.67)
```

## 3rd run

```bash
❯ pylint analyze_image.py
************* Module scr.analyze_image
analyze_image.py:58:4: R0914: Too many local variables (17/15) (too-many-locals)
analyze_image.py:115:15: W0718: Catching too general exception Exception (broad-exception-caught)
analyze_image.py:89:27: W3101: Missing timeout argument for method 'requests.post' can cause your program to hang indefinitely (missing-timeout)
analyze_image.py:58:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)

------------------------------------------------------------------
Your code has been rated at 9.17/10 (previous run: 8.97/10, +0.20)
```

- R0914: Too many local variables (17/15)
- W0718: Catching too general exception Exception
- R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
- W3101: Missing timeout argument for method 'requests.post' can cause your program to hang indefinitely (missing-timeout)

Theses issues need to be fixed in the code in a future update.
