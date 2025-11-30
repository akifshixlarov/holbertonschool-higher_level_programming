#!/usr/bin/env python3
"""Basic JSON serialization/deserialization functions"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes Python data to JSON and saves it to a file.

    Args:
        data (any): Python object to serialize
        filename (str): Path to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into Python.

    Args:
        filename (str): Path to JSON file

    Returns:
        any: Python object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
