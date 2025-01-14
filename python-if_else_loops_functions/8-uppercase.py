#!/usr/bin/python3
def uppercase(str):
    result = ""  # variable qui va contenir la str transformée en MAJ
    for char in str:  # parcourt la chaine
        if ord('a') <= ord(char) <= ord('z'):  # si minuscule
            result += chr(ord(char) - 32)  # transforme en MAJ, stock dans res
        else:
            result += char  # sinon stock direct dans result
    print(result)
