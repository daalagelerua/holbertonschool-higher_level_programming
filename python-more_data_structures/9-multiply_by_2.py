#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    dico = {}

    for key, value in a_dictionary.items():
        dico[key] = value * 2

    return dico
