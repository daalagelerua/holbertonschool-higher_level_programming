#!/usr/bin/python3
"""
This module cfreates an object from json file
"""
import os
import json


def load_from_json_file(filename):
    """
    This function creates an object from a json file
    Args:
        filename (str): name of file

    Returns:
        str: object
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
