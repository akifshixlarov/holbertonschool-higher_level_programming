#!/usr/bin/env python3
"""Pickle serialization/deserialization for CustomObject"""

import pickle


class CustomObject:
    """A class that supports pickling and unpickling"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file using pickle.

        Args:
            filename (str): File to write to
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a pickle file.

        Args:
            filename (str): File to read from

        Returns:
            CustomObject: Loaded object
        """
        with open(filename, "rb") as f:
            return pickle.load(f)
