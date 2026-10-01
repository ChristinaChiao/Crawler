#實作題：任務一
import csv
products = [{"ID":"A001", "Name":"蘋果", "Price": 350},
            {"ID":"A002", "Name":"香蕉", "Price": 210},
            {"ID":"A003", "Name":"櫻桃", "Price": 500}]
for item in products: 
    with open("C:\\Users\\User\\venvShao\\PythonCode\\HW\\HW-ch02products.csv", mode='a', encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Price'])
        writer.writerow(item)
        print("Done")