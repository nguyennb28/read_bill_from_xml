import xml.etree.ElementTree as ET
import os

namespace = {"inv": "http://laphoadon.gdt.gov.vn/2014/09/invoicexml/v1"}
results = []

for filename in os.listdir():
    if filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()

        # Lấy tất cả itemName (cả có namespace và không)
        invoice_names = [elem.text for elem in root.findall(".//inv:itemName", namespace) if elem.text]
        invoice_names += [elem.text for elem in root.findall(".//THHDVu") if elem.text]

        # Lấy shdon_value
        invoice_number_elem = root.find(".//inv:invoiceNumber", namespace)
        shdon_value = invoice_number_elem.text if invoice_number_elem is not None else None
        if not shdon_value:
            for elem in root.iter():
                if elem.tag.startswith("SHDon") and elem.text:
                    shdon_value = elem.text
                    break

        # Lấy total_value
        invoice_total_elem = root.find(".//inv:totalAmountWithVAT", namespace)
        total_value = invoice_total_elem.text if invoice_total_elem is not None else None
        if not total_value:
            for elem in root.iter():
                if elem.tag.startswith("TgTTTBSo") and elem.text:
                    total_value = elem.text
                    break

        # Chỉ thêm vào kết quả nếu có đủ thông tin
        if shdon_value and total_value:
            results.append(
                {"itemName": invoice_names, "shdon": shdon_value, "total": total_value}
            )

for x in results:
    print(x)