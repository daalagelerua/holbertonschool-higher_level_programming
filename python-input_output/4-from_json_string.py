#!/usr/bin/python3
"""
This module returns an object
"""
import json


def from_json_string(my_str):
    """
    This function returns an object from a json
    Args:
        my_str (str): json rep
    Returns:
        str: object
    """
    return json.loads(my_str)
