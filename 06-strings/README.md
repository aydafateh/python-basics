# 06 — Strings

A collection of string exercises: counting, replacing, filtering, validating, and compressing text.

## Files

| File | Description | Concepts |
|---|---|---|
| `count_letter_a.py` | Count occurrences of "a" | str.count |
| `count_specific_chars.py` | Count a, e, i | str.count |
| `count_vowels.py` | Count vowels in a sentence | for, in |
| `email_validator.py` | Validate a Gmail-style email | split, endswith, isidentifier |
| `filter_python.py` | Remove "python" from text | lower, replace |
| `password_validator.py` | Check password for length, cases, digits, symbols | set, sets intersection |
| `phone_validator_ir.py` | Validate Iranian mobile numbers (MCI, Irancell, Rightel) | startswith, in, len |
| `replace_python.py` | Replace "python" with "programming" | replace |
| `sentence_counter.py` | Count sentences by splitting on . ! ? ; | split |
| `string_compressor.py` | Compress "aaabb" → "a3b2" | for, string building |
| `trim_spaces.py` | Strip extra spaces | strip |
| `word_counter.py` | Count alphabetic words | split, isalpha |

## Notes

`sentence_counter.py` uses `len(...) - 4`, which is fragile. Better to split with `re.split(r'[.!?;]', text)` and filter empty parts.