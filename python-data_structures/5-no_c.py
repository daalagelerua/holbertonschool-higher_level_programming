#!/usr/bin/python3
def no_c(my_string):

    my_string = [item for item in my_string if item != 'c' and item != 'C']
    return (' '.join(my_string))
