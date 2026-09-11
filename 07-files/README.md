# 07 — Files

A console contact manager that stores users and contacts in text files.

## Files

| File | Description | Concepts |
|---|---|---|
| `mobilecontacts.py` | Full contact book with login, register, add, list, search | Files, functions, validation, os, platform |

## Data files (created at runtime)

- `users.txt` — `username:password` per line
- `contacts.txt` — `first last phone email` per line

## Notes

- Passwords are stored in plain text. For learning it's fine, but never do this in real apps.
- `validate_password` returns `False` (a single value) in some branches and `(False, "message")` in others. This makes `if validate_password(...)` sometimes behave unexpectedly. Return a consistent `(bool, message)` tuple everywhere.
- Uses `open(...)` without `with`. Prefer `with open(...) as f:` to auto-close files.