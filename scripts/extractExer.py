#!/usr/bin/env python3


import sys


content=[]
exercises=['<?xml version="1.0" encoding="UTF-8"?>\n']
inexer=0

with open(sys.argv[1], 'r') as my_file:
    lines = my_file.readlines()
    my_file.close()
    for line in lines:
    	if line.find("<section xml:id") != -1:
    		line=line.replace('<section ', '<section xmlns:xi="http://www.w3.org/2001/XInclude" ')
    		print("new starting line:\n"+line)

    	if (line.find("<exercises>") != -1): inexer=1

    	if inexer==0: content.append(line)
    	else:
    		if line[:2]=="  ": line=line[2:] #deleting first occurrence of tab in exercise lines.
    		exercises.append(line)

    	if (line.find("</exercises>") != -1): 
    		inexer=0
    		content.append('  <xi:include href="exer_'+ sys.argv[1] +'" />\n')
    		print("added exercise include at line {}".format(len(content)) )


if len(exercises)>1:
	print("found exercises!\n {} lines of content \n {} lines of exercises".format(len(content), len(exercises)) )
else:
	print("no exercises")

resp = input("pause to make sure that looks right")


# writing to file
with open(sys.argv[1], 'w') as contentFile:
	contentFile.writelines(content)
	contentFile.close()
 
with open("exer_"+sys.argv[1], 'w') as exerFile:
	exerFile.writelines(exercises)
	exerFile.close()
