#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # create a new list to store true or false for each element
    result = []

    for l in my_list:
        if l % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
