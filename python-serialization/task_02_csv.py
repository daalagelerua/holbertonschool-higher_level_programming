#!/usr/bin/python3
"""
This module defines a function that convert csv to json
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    This function convert csv to json
    Args:
        filename (str): name of file
    """
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False