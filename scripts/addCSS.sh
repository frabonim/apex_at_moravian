#!/bin/zsh

rep="s|</head>|<link rel=\"stylesheet\" type=\"text/css\" href=\"./$2\">\n<link rel=\"shortcut icon\" href=\"https://webwork.moravian.edu/apexcalc/external/muFaviconStar.png\" /></head>|"

for f in $1/*.html; do
	sed -i '' "$rep" $f
done