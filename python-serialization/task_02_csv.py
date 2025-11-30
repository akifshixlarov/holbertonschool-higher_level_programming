#!/usr/bin/env python3
"""Convert CSV data to JSON and save as data.json"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): Path to the CSV file

    Returns:
        bool: True if conversion succeeds, False otherwise
    """
    try:
        data_list = []

        # Read CSV
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(dict(row))

        # Write JSON
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
