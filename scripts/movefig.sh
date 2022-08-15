#!/bin/bash

if [ -e "../APEXCalculusV5/figures/$1.pdf" ]
then
  cd src/images;
  cp ../../../APEXCalculusV5/figures/$1.* .;
  pdf2svg $1.pdf $1.svg;
  cd ../../
else
    echo "can't find that file"
fi
