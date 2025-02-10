#!/usr/bin/python3

import os


def read_file(filename=""):
    with open("0-read_file.txt", "r", encoding="utf-8") as file:
        print(file.read(), end="")