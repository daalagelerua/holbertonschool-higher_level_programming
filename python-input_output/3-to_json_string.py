#!/usr/bin/python3
"""
This module returns the json representation of an object
"""
import json

def to_json_string(my_obj):
    """
    This function returns json rep of obj
    Args:
        my_obj (str): object to represent

    Returns:
        str: rep of obj
                """
    return json.dumps(my_obj)