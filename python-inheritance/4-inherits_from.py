#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Check if object is instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited (directly or
        indirectly) from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
