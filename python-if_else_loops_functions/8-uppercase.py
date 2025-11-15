#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print()
