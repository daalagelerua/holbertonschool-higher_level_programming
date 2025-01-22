#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # sort keys alphabetically
    dico = sorted(a_dictionary.keys())

    for key in dico:
        print("{}: {}".format(key, a_dictionary[key]))
