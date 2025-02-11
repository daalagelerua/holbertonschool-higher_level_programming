#!/usr/bin/python3
"""
This module appends to a file
"""
import os


def append_write(filename="", text=""):
    """
    This function appends text to a file
    Args:
        filename (str): name of file. Defaults to "".
        text (str): text to append. Defaults to "".

    Returns:
        str: new text
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
