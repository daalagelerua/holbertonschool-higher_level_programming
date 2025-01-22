#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
'''
map apply function for each element of iterable & return iterator
x represent each element of my_list
list() convert iterator in a list
'''
    return list(map(lambda x: x * number, my_list))
