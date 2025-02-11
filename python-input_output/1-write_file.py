#!/usr/bin/python3
"""
This module write a file
"""
import os


def write_file(filename="", text=""):
    """
    This function write a file
    Args:
        filename (str): name of file. Defaults to "".
        text (str): text of the file. Defaults to "".

    Returns:
        str: new text
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)