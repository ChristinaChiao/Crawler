import json
import csv
file = r"C:\Users\User\venvShao\PythonCode\ch03\ch03-1-6.json" #加r就不用\\
with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    
with open(r"C:\Users\User\venvShao\PythonCode\ch03\ch03-1-6.csv", mode="w", encoding="utf-8-sig", newline='') as f:
  filename = ["title", "click"]
  writer = csv.DictWriter(f, fieldnames=filename)
  writer.writeheader()
  writer.writerows(data)