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
total_list = []


for filename in os.listdir():
    if filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        hd = ""
        total = ""

        for elem in root.iter():
            if elem.tag.startswith("SHDon") and elem.text:
                hd = elem.text
                SHDon_list.append(elem.text)
            if elem.tag.startswith("TgTTTBSo"):
                total = elem.text
                total_list.append(elem.text)
            if hd and total:
                print(f"hd: {hd}")
                print(f"total: {total}")

            # if hd == "" or total == "":
            #     continue
            # else:
            #     results.append({"SHDon": hd, "Total": total})
            # if elem.tag.startswith("SHDon") and elem.text:

        invoice_number_elem = root.find(".//inv:invoiceNumber", namespace)
        invoice_number = (
            invoice_number_elem.text if invoice_number_elem is not None else None
        )
        if invoice_number:
            SHDon_list.append(invoice_number)
            results.append({"SHDon": invoice_number, "Total": "1000.000"})

        invoice_total_amount_elem = root.find(".//inv:totalAmountWithVAT", namespace)
        invoice_total = (
            invoice_total_amount_elem.text
            if invoice_total_amount_elem is not None
            else None
        )
        if invoice_total:
            total_list.append(invoice_total)

# print(SHDon_list)
# print(results)
# print(SHDon_list)
# print(total_list)
