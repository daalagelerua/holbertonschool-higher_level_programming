#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    uncommon_set = set()

    # Iterate over each element in the first set
    for element in set_1:
        # Check if the element is not in the second set
        if element not in set_2:
            # If it's not, add it to the uncommon set
            uncommon_set.add(element)
    # repeat in reverse
    for element in set_2:
        if element not in set_1:
            uncommon_set.add(element)

    # Return the set of uncommon elements
    return uncommon_set
