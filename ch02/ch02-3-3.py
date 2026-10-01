import xml.etree.ElementTree as ET

tree = ET.parse('ch02/files/clinic.xml')
root = tree.getroot()
print("---診所列表---")

for clinic in root.findall("Data"):  #XML實際標籤是<Data>
    print("診所名稱=", clinic.find("機構名稱").text)
    print("電話=", clinic.find("電話").text)
    print("-" * 30) 