#!/bin/bash

## use this to generate just one picture from latex source.  As a command
## line arg, use the xml:id of the image, or even of a section.

../mathbook/script/mbx -c latex-image -f svg -r $1 -d output/images/ src/index.ptx
cp output/images/$1.svg output/html/images/
