import xml.etree.ElementTree as ET
import os

namespace = {"inv": "http://laphoadon.gdt.gov.vn/2014/09/invoicexml/v1"}
"""
    Output: [{
        "SHDon": value,
        "Total": value,   
    }]
"""

results = []
SHDon_list = []

for filename in os.listdir():
    if filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()

        for elem in root.iter():
            if elem.tag.startswith("SHDon"):
                if elem.text:
                    SHDon_list.append(elem.text)
                    results.append({"SHDon": elem.text, "Total": "1000.000"})

        invoice_number_elem = root.find(".//inv:invoiceNumber", namespace)
        invoice_number = (
            invoice_number_elem.text if invoice_number_elem is not None else None
        )
        if invoice_number:
            SHDon_list.append(invoice_number)
            results.append({"SHDon": invoice_number, "Total": "1000.000"})

print(results)

