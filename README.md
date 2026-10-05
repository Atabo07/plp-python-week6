# Week 6 Assignment - Catching Errors with try / except

- `safe_tools.py` - three safe functions (`safe_divide`, `safe_number`, `get_field`) that return a friendly message instead of crashing.
- `unbreakable.py` - an input loop that keeps running, using `try`/`except` for bad input and an `if` check for unwise input.

## Why can the `if` check not catch `abc` on its own?

An `if` check can only compare a value that already exists, but `int("abc")` fails *before* there is a number to check, so the program crashes on that line and the `if` never runs. A `try`/`except ValueError` is needed to catch that failure, while the `if` is for unwise-but-valid numbers (like an age of -5).
