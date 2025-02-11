#!/usr/bin/python3
"""
This module read a file
"""
import os


def read_file(filename=""):
    """
    the function reads a file
    Args:
        filename (str): name of file. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
