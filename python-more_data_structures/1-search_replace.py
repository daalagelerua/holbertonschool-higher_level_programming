#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []
    for element in my_list:
        # if the element matches the search element, replace it in new_list
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
