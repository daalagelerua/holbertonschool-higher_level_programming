#!/usr/bin/python3
"""
This function `text-indentation` takes a string
and print it with indentation every '?', '.', ':'.
"""


def text_indentation(text):
    """
    Print a text with indentation.

    Parameters:
    text: string to print.

    Raises:
    TypeError: If 'text' is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
