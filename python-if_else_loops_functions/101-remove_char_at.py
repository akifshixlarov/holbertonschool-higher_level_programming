#!/usr/bin/python3
def remove_char_at(str, n):
    """Return a copy of `str` without the character at index `n`."""
    if n < 0 or n >= len(str):
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
