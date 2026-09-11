# 05 — Dictionaries

A small Finglish-to-Persian word translator using a dictionary.

## Files

| File | Description | Concepts |
|---|---|---|
| `finglish_to_persian.py` | Translate a Finglish word to Persian | dict, key lookup |

## Notes

`words_dict[word]` will raise `KeyError` if the word is not found. Use `words_dict.get(word, "not found")` to handle missing words gracefully.