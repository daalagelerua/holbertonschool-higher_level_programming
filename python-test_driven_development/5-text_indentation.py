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
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end="")
            i += 1
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
