#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A BaseGeometry class with an area method."""

    def area(self):
        """Raise an exception indicating area is not implemented.

        Raises:
            Exception: Always raises with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
