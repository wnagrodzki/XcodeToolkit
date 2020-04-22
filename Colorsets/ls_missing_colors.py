#!/usr/bin/env python3

""" Searches xib and storyboard files for missing colors.

If a named color is used in user interface file, and it is not present in 
asset catalog it is considered missing.
"""

import os
import pathlib
import xml.etree.ElementTree

# Find colors

known_colors = []

for dirpath, dirnames, filenames in os.walk('.'):
    pure_path = pathlib.PurePath(dirpath)
    directory_name = pure_path.name
    if '.colorset' in directory_name:
        known_colors.append(pure_path.stem)

# Find user interface files

filepaths = []

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        name_path = pathlib.PurePath(filename)
        if name_path.suffix in [".xib", ".storyboard"]:
            filepath = os.path.join(dirpath, name_path)
            filepaths.append(filepath)

# Check if user interface files contain unknown colors

for filepath in filepaths:
    tree = xml.etree.ElementTree.parse(filepath)
    root = tree.getroot()
    resources = root.find("resources")
    if resources is None:
        continue
    for named_color in resources.findall("namedColor"):
        color_name = named_color.get("name")
        if color_name not in known_colors:
            message = "warning: missing color: " + color_name + " used in: " + pathlib.PurePath(filepath).name
            print(message)
