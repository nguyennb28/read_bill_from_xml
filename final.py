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
# invoice_names = []
my_list = [1, 2, 3, 4, 5]

for filename in os.listdir():
    if filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()

        # INVOICE NAME
        # invoice_names_values = [
        #     elem.text for elem in root.findall(".//THHDVu") if elem.text
        # ]
        # invoice_names_values += [
        #     elem.text
        #     for elem in root.findall(".//inv:itemName", namespace)
        #     if elem.text
        # ]
        # invoice_names.append(invoice_names_values)

        # INVOICE ELEMENT
        invoice_number_elem = root.find(".//inv:invoiceNumber", namespace)
        shdon_value = (
            invoice_number_elem.text if invoice_number_elem is not None else None
        )

        if not shdon_value:
            for elem in root.iter():
                if elem.tag.startswith("SHDon") and elem.text:
                    shdon_value = elem.text
                    break

        # INVOICE TOTAL
        invoice_total_elem = root.find(".//inv:totalAmountWithVAT", namespace)
        total_value = (
            invoice_total_elem.text if invoice_total_elem is not None else None
        )

        if not total_value:
            for elem in root.iter():
                if elem.tag.startswith("TgTTTBSo") and elem.text:
                    total_value = elem.text
                    break

        # INVOICE NAME "SHDon"
        invoice_names = []
        for elem in root.iter():
            # INV = elem.findall(".//inv:itemName", namespace)
            if elem.tag.startswith("THHDVu") and elem.text:
                invoice_names.append(str(elem.text))
            # elif INV:
                # for index,x in enumerate(INV):
                    # print(index)
                    # print(x.text)
            else:
                continue
                

        if shdon_value and total_value:
            results.append({"itemName": invoice_names, "shdon": shdon_value, "total": total_value})


# for x in results:
    # print(x)