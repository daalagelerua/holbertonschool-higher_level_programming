#!/usr/bin/python3
class VerboseList(list):
    for element in list:
        if super().append(element):
            print(f"Added {[element]} to the list.")
        if super().remove(element):
            print(f"Removed {[element]} from the list.")
        if super().pop(element):
            print(f"Popped {[element]} from the list.")
    for nb in range(len(list)):
        if super().extend(nb):
            print(f"Extended the list with {[nb]} items.")