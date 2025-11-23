#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and its first character.
               If the string is empty, the first character is set to None.
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
