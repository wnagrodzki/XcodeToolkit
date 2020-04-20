#!/bin/zsh

GENERATED_FILE_LOCATION=`mktemp`
COLORS_FILE_LOCATION="UIColor+Colorsets.swift"

./uicolor_colorsets.py > $GENERATED_FILE_LOCATION
./cp_if_different.sh $GENERATED_FILE_LOCATION $COLORS_FILE_LOCATION