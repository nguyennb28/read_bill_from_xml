import xml.etree.ElementTree as ET
import os

thislist = []
SHDon = []
for x in os.listdir():
    if x.endswith(".xml"):
        thislist.append(x)


for file in thislist:
    tree = ET.parse(file)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag == "SHDon":
            SHDon.append(elem.text)

print(SHDon)