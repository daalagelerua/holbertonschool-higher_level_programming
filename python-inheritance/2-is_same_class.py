#!/usr/bin/python3
"""
This module defines a function that checks an instance
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is an exact
    instance of a class
    Args:
        obj (): object
        a_class (): class
    """
    return type(obj) is a_class
