#!/usr/local/bin/python3

from xml.etree import ElementTree
import sys
#filename=sys.argv[1]


# Turn "None" int an empty string
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


root = ElementTree.parse(sys.stdin).getroot()

indent(root)

#make a map of all parents to use later
parent_map = {c:p for p in root.iter() for c in p}

#"figure" should be a sidebyside with image
for i in root.iter():
    fig=i.find('figure')
    if fig is None: continue
    figname=fig.get('file')
    if figname is None: continue
    figname=figname.replace('figures/', 'images/')
    par=parent_map[fig]
    newsidebyside=ElementTree.SubElement(par, 'sidebyside', {'width':'30%'})
    ElementTree.SubElement(newsidebyside, 'image', {'source':figname})
    par.remove(fig)

#ElementTree.dump(root)

## the lazy way to rename the <std> fake root element.
final=ElementTree.tostring(root, encoding="utf-8").decode("utf=8")
lines = final.splitlines()
print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
for line in lines:
    line=line.replace("<std>", "<section>")
    line=line.replace("</std>", "</section>")
    print(line)




