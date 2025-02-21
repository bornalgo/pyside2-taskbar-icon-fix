#!/bin/bash

LOGO=res/bal
ICONS=()
# sudo apt-get install inkscape
for sz in 256 64 48 40 32 24 20 16 ; do
  inkscape -w $sz -h $sz -o "${LOGO}_${sz}.png" "${LOGO}.svg"
  ICONS=("${ICONS[@]}" "${LOGO}_${sz}.png")
done
# sudo apt-get install imagemagick
convert "${ICONS[@]}" "${LOGO}.ico"

identify "${LOGO}.ico"