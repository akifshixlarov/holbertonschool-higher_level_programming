#!/usr/bin/python3
def no_c(my_string):
    """Return a new string with all 'c' and 'C' removed."""
    new_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
