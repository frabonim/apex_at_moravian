#!/bin/zsh

rep="s|</head>|<link rel=\"stylesheet\" type=\"text/css\" href=\"./$2\">\n</head>|"

for f in $1/*.html; do
	sed -i '' "$rep" $f
done