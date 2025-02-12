#!/usr/bin/python3
"""
This module defines a 
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function serializes a dict to xml
    Args:
        dictionary (dict): dict to serialize
        filename (str): name of file
    """
    root = ET.Element("root")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration=True)

def deserialize_from_xml(filename):
    """
    This function deserializes a xml file
    Args:
        filename (str): name of file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {child.tag: child.text for child in root}
    return dictionary