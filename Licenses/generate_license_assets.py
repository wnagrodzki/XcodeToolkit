#!/usr/bin/env python3

"""Generates a set of files for Settings.bundle in order to display a list of dependency licenses used in the application.
Liceses will be listed in Settings > Your Application > Third-Party Notices and/or Licenses.
1) Move Licenses.plist and Licenses directory into Settings.bundle.
2) Add entry referencing Licenses in Root.plist.

<key>PreferenceSpecifiers</key>
<array>
    <dict>
        <key>File</key>
        <string>Licenses</string>
        <key>Title</key>
        <string>Third-Party Notices and/or Licenses</string>
        <key>Type</key>
        <string>PSChildPaneSpecifier</string>
    </dict>
</array>
"""

import os
import pathlib

license_list_template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PreferenceSpecifiers</key>
    <array>
        ITEMS_PLACEHOLDER
    </array>
</dict>
</plist>
"""

license_list_item_template = """
        <dict>
            <key>File</key>
            <string>license_text_file_path_PLACEHOLDER</string>
            <key>Title</key>
            <string>ITEM_TITLE_PLACEHOLDER</string>
            <key>Type</key>
            <string>PSChildPaneSpecifier</string>
        </dict>
"""

license_template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PreferenceSpecifiers</key>
    <array>
        <dict>
            <key>FooterText</key>
            <string>LICENSE_TEXT_PLACEHOLDER</string>
            <key>Type</key>
            <string>PSGroupSpecifier</string>
        </dict>
    </array>
</dict>
</plist>
"""

licenses_directory_name = "Licenses"
if not os.path.exists(licenses_directory_name):
    os.mkdir(licenses_directory_name)

license_list_items = []

for name in os.listdir(path='.'):

    directory = name
    if not os.path.isdir(directory):
        continue

    license_text_file_path = os.path.join(directory, "LICENSE")
    if not os.path.isfile(license_text_file_path):
        continue
    
    license_path_no_extension =  licenses_directory_name + "/" + directory

    license_list_item = license_list_item_template
    license_list_item = license_list_item.replace("license_text_file_path_PLACEHOLDER", license_path_no_extension)
    license_list_item = license_list_item.replace("ITEM_TITLE_PLACEHOLDER", directory)
    license_list_items.append(license_list_item)

    with open(license_text_file_path, 'r') as license_text_file:
        license_text = license_text_file.read()
        license = license_template.replace("LICENSE_TEXT_PLACEHOLDER", license_text)
        license_path = license_path_no_extension + ".plist"

        license_file = open(license_path, "w")
        license_file.write(license)
        license_file.close()


license_list_items_string = "".join(license_list_items)
license_list = license_list_template.replace("ITEMS_PLACEHOLDER", license_list_items_string)

license_list_path = "Licenses.plist"
license_list_file = open(license_list_path, "w")
license_list_file.write(license_list)
license_list_file.close()
