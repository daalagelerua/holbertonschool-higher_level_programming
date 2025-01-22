#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over each element in the list
    for element in my_list:
        # Add the element to the set (duplicates are automatically ignored)
        unique_integers.add(element)

    # Sum all the unique integers in the set
    total = sum(unique_integers)

    # Return the total
    return total
