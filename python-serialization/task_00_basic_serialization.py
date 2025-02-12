#!/usr/bin/python3
"""
This module defines 2 function that serializes and
deserializes data
"""

import json
import os


def serialize_and_save_to_file(data, filename):
    """
    This function writes and save an object from a text file
    using json rep
    Args:
        data (dict): object
        filename (str): name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    This function creates an object from a json file
    Args:
        filename (str): name of file

    Returns:
        dict: object
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
