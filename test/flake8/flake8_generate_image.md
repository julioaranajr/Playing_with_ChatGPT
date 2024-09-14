# Flake8 Report - Module to generate images using OpenAI's DALL-E model

## 1st.Run

```bash
❯ flake8 generate_image.py
generate_image.py:1:1: D200 One-line docstring should fit on one line with quotes
generate_image.py:6:1: I201 Missing newline between import groups. 'from openai import OpenAI' is identified as Third Party and 'import os' is identified as Stdlib.
generate_image.py:7:1: I100 Import statements are in the wrong order. 'from PIL import Image' should be before 'from openai import OpenAI' and in a different group.
generate_image.py:7:1: I201 Missing newline between import groups. 'from PIL import Image' is identified as Third Party and 'from openai import OpenAI' is identified as Third Party.
generate_image.py:8:1: I201 Missing newline between import groups. 'import requests' is identified as Third Party and 'from PIL import Image' is identified as Third Party.
generate_image.py:9:1: I201 Missing newline between import groups. 'from stringcolor import cs' is identified as Third Party and 'import requests' is identified as Third Party.
generate_image.py:12:11: Q000 Double quotes found but single quotes preferred
generate_image.py:12:22: Q000 Double quotes found but single quotes preferred
generate_image.py:12:36: Q000 Double quotes found but single quotes preferred
generate_image.py:20:1: D200 One-line docstring should fit on one line with quotes
generate_image.py:24:1: D107 Missing docstring in __init__
generate_image.py:24:43: Q000 Double quotes found but single quotes preferred
generate_image.py:28:1: D105 Missing docstring in magic method
generate_image.py:29:16: Q000 Double quotes found but single quotes preferred
generate_image.py:32:1: D200 One-line docstring should fit on one line with quotes
generate_image.py:35:18: Q000 Double quotes found but single quotes preferred
generate_image.py:35:35: Q000 Double quotes found but single quotes preferred
generate_image.py:37:56: Q000 Double quotes found but single quotes preferred
generate_image.py:37:77: Q000 Double quotes found but single quotes preferred
generate_image.py:37:80: E501 line too long (80 > 79 characters)
generate_image.py:41:56: Q000 Double quotes found but single quotes preferred
generate_image.py:41:62: Q000 Double quotes found but single quotes preferred
generate_image.py:43:80: E501 line too long (80 > 79 characters)
generate_image.py:46:31: Q000 Double quotes found but single quotes preferred
generate_image.py:52:16: Q000 Double quotes found but single quotes preferred
generate_image.py:53:20: Q000 Double quotes found but single quotes preferred
```

- D200: One-line docstring should fit on one line with quotes
- I201: Missing newline between import groups
- I100: Import statements are in the wrong order
- Q000: Double quotes found but single quotes preferred
- D107: Missing docstring in **init**
- D105: Missing docstring in magic method
- E501: Line too long (80 > 79 characters)

All issues was fixed in the code.Now the code is clean and ready to be used.
