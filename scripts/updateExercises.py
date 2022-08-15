#!/usr/local/bin/python3

## wipes out the current exercises element, then puts in
## an include to a file in ./exercises/ with similar name

from xml.etree import ElementTree
import sys, os
from shutil import copy


# Turn "None" into an empty string
def xstr(s):
    if s is None:
        return ''
    return str(s)

def indent(elem, level=0, more_sibs=False):
    i = "\n"
    if level:
        i += (level-1) * '  '
        ip1 = "\n" + (level+1)* '  '
    num_kids = len(elem)

    # p is special, I don't really want to process its children
    # the only exception is md.  how to deal with that??
    # is it better to have a whitelist or blacklist for children of p?
    if elem.tag == "p" and elem.text:
        elem.text = ip1 + elem.text
        if num_kids:
            elem[-1].tail = xstr(elem[-1].tail) + i + '  '
        else:
            elem.text = elem.text + ip1
        for kid in elem:
            if kid.tag == "md": # md is only thing I will indent in p
                indent(kid, level+1)
                kid.tail=ip1+kid.tail
        num_kids = 0;  # stop checking children in p.

    if num_kids:
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
            if level:
                elem.text += '  '
        count = 0
        for kid in elem:
            indent(kid, level+1, count < num_kids - 1)
            count += 1
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
            if more_sibs:
                elem.tail += '  '
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            if more_sibs:
                elem.tail += '  '





expath='/Users/memjf02/books/apex-mbx-master/src/exercises/'
destpath='/Users/memjf02/books/apex-mbx-master/src/'
backup=destpath+'original/'

#ignore any leading path
destName=os.path.basename(sys.argv[1])
dest=destpath+destName
source="exer_"+destName[:-4]+".ptx"
if not(os.path.isfile(backup+destName)):
    print("couldn't find file %s" % dest)
    sys.exit()

with open(backup+destName, 'r') as fp:
    lines = fp.read()


#root = ElementTree.parse(lines).getroot()
root = ElementTree.fromstring(lines)

ex=root.find("exercises")
if ex==None:
    print('warning: no <exercises> in %s.' % destName)
else:
    root.remove(ex)
    ElementTree.SubElement(root, 'xi:include', {'href':'exercises/'+source})

root.attrib['xmlns:xi']='http://www.w3.org/2001/XInclude'
indent(root)
final="<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
final="%s\n%s" % (final, ElementTree.tostring(root, encoding="utf-8").decode("utf=8"))

with open(dest, 'w') as fp:
    fp.write(final)
#print(final)

## a little more post-processing for my conversion attempts
#final=ElementTree.tostring(root, encoding="utf-8").decode("utf=8")
#lines = final.splitlines()
#print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
#for line in lines:
#    line=line.replace('<section xml:id=', '<section xmlns:xi="http://www.w3.org/2001/XInclude" xml:id=')
#    line=line.replace("<MYinclude", "<xi:include")
#    print(line)

