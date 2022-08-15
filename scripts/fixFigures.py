#!/usr/local/bin/python3
import sys, os
import re
from shutil import copy


figbase='/Users/memjf02/books/APEXCalculusV5/figures/'
destbase='/Users/memjf02/books/apex-mbx-master/src/'
backup=destbase+'bak/'
figdest=destbase+'images/'


filearg=sys.argv[1]
filename=os.path.basename(filearg)
try:
	copy(filearg, backup+filename)
except:
	print('\n****--------- cannot copy '+m[1]+'.pdf  -------***\n')
	sys.exit()

with open(backup+filename, 'r') as fp:
    lines = fp.read()



reReplace = re.compile('<!-- START figures/([^.]*?)\.asy -->\s*?<image (xml:id=".*?") >.*?<!--.*?END -->',re.DOTALL)

def processMatch(m):
	print("looking for "+figbase+m[1])
	try:
		copy(figbase+m[1]+'.pdf', figdest)
		print("    - found .pdf")
	except:
		print('\n\n!!!!!!!--------- cannot copy '+m[1]+'.pdf  -------!!!!!!!!\n\n')
		input("Press Enter if you want to continue anyway, ^C to stop...")
	for ext in ['.asy','.prc']:
		try:
			copy(figbase+m[1]+ext, figdest)
			print("    - found "+ext)
		except:
			print('\n\n!!!!!!!--------- cannot copy '+m[1]+ext+'  -------!!!!!!!!\n\n')
	try:
		#execute pdf2svg figdest+m[1]+'.pdf' figdest+m[1]+'.svg'
		os.system('pdf2svg '+figdest+m[1]+'.pdf '+figdest+m[1]+'.svg')
		print("    - converted .svg")
	except:
		print('\n warn: could not convert '+m[1]+'.pdf to an svg')
	return('<image '+m[2]+' source="images/'+m[1]+'" /> <!-- TODO: make this moveable with asy or prc -->')


lines=reReplace.sub(processMatch, lines)

input("Press Enter if you are ready to write to the file, ^C otherwise...")

with open(filearg, 'w') as output:
	output.write(lines)
#print(lines)

