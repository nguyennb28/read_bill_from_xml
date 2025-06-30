import xml.etree.ElementTree as ET
import os

thislist = []
for x in os.listdir():
    if x.endswith(".xml"):
        thislist.append(x)


namespace = {"inv", "http://laphoadon.gdt.gov.vn/2014/09/invoicexml/v1"}

for file in thislist:
    tree = ET.parse(file)
    root = tree.getroot()
    print(root)
