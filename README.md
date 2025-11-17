# code-phantom-x-v1
ai tools
# Code Phantom X v1.1

**Invisible AI Assistant for Python Developers – Ghost Pair Programming!**

This tool interactively analyzes your Python code: while you type, _Phantom_ catches frequent bugs, and _Ghost_ suggests improvements like a senior developer.

## Features

- **Interactive mode**
  - Type your code line by line; Phantom and Ghost analyze it in real time
  - Easy workflow – finish your input with two empty lines
- **Phantom AI**
  - Automatically detects typical mistakes, such as:
    - Using `=` instead of `==`
    - Debug prints in production code
    - TODO comments
    - Empty `pass` blocks
    - Overly long functions
- **Ghost AI**
  - Suggests improvements for code style and testing:
    - Type hinting
    - Writing docstrings
    - Adding unittests
    - Better inline comments
    - Using list comprehensions

## Usage

```bash
python code_phantom_x.py
```

Follow the interactive instructions:
- Type your code line-by-line.
- When you're done, press Enter twice.
- To exit, type `exit`.

## Example Session

```
Your code:
def add(a, b):
    return a = b  # Error!

[12:01] [PHANTOM  ] Line 2: You're using '=' instead of '==' – likely a mistake!
[12:01] [GHOST    ] Add type hints: def add(x: int) -> int:
```

## Requirements

- Python 3.6+

## Feedback & Contributions

Open an issue or submit a PR!

---

© 2025 Kokalohf
