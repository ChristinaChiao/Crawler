import csv
import os

data = [{"品名":"台積電", "股價": 800, "評等": "買進"},
        {"品名":"聯發科", "股價": 1000, "評等": "持有"},
        {"品名":"鴻海", "股價": 150, "評等": "買進"}]
file_name = "ch02/files/stocks_2-1-try.csv"

with open(file_name, mode = "w", encoding="utf-8-sig", newline="")as file: #寫入資料，用open做出的檔案文件
    #沒有加-sig會導致Excel打開時中文亂碼
    file_names = ["品名", "股價", "評等"]
    writer = csv.DictWriter(file, fieldnames=file_names) #將字典中的資料匯出為CSV
    writer.writeheader()
    writer.writerows(data)

with open(file_name, mode = "r", encoding="utf-8-sig")as file:
    reader = csv.DictReader(file) #變成字典格式
    for row in reader:
        print(row)
        
new_data = {"品名":"新產品", "股價": 500, "評等": "觀察"}
not_exist = False

if not os.path.exists(file_name):  #追加時，避免重複寫入表頭
    not_exist = True
    
with open(file_name, mode = "a", encoding="utf-8-sig", newline="")as file: #寫入資料，用open做出的檔案文件
    #沒有加-sig會導致Excel打開時中文亂碼
    file_names = ["品名", "股價", "評等"]
    writer = csv.DictWriter(file, fieldnames=file_names) #將字典中的資料匯出為CSV
    if not_exist:  #避免重複寫入表頭
      writer.writeheader() 
    writer.writerow(new_data)