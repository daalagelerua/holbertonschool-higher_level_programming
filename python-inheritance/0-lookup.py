#!/usr/bin/python3
"""
This module defines a function that lists attributes
"""


def lookup(obj):
    """
    This function returns a list of available
    attributes and method of an object
    Args:
        obj (): object

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
