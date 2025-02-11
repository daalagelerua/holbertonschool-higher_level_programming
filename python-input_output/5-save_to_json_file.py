#!/usr/bin/python3
"""
This module writes an object to a text file
"""
import os
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object from a text file
    using json rep
    Args:
        my_obj (str): object
        filename (str): name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
