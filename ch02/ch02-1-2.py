import csv
import os

new_data = {"品名":"台積電", "股價": 800, "評等": "買進"}
file_name = "ch02/files/stocks_2-1-2.csv"

#寫法1
with open(file_name, mode = "a", encoding="utf-8-sig", newline="")as file: #寫入資料，用open做出的檔案文件
    #沒有加-sig會導致Excel打開時中文亂碼
    file_names = ["品名", "股價", "評等"]
    writer = csv.DictWriter(file, fieldnames=file_names) #將字典中的資料匯出為CSV

    if not os.path.exists(file_name):  #追加時，避免重複寫入表頭
      writer.writeheader() 
    writer.writerow(new_data)

#寫法2
not_exist = False
if not os.path.exists(file_name):  #追加時，避免重複寫入表頭
    not_exist = True
    
with open(file_name, mode = "a", encoding="utf-8-sig", newline="")as file: #寫入資料，用open做出的檔案文件
    #沒有加-sig會導致Excel打開時中文亂碼
    file_names = ["品名", "股價", "評等"]
    writer = csv.DictWriter(file, fieldnames=file_names) #將字典中的資料匯出為CSV
    if not_exist: 
      writer.writeheader() 
    writer.writerow(new_data)