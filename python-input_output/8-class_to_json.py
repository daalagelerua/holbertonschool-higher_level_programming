#!/usr/bin/python3
"""
This module returns a dictionnary
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for
    JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes
        (list, dict, str, int, bool).

    Returns:
        dict: A dictionary containing all serializable attributes of object.
    """

    return vars(obj)
