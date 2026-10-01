import csv

data = [{"品名":"台積電", "股價": 800, "評等": "買進"},
        {"品名":"聯發科", "股價": 1000, "評等": "持有"},
        {"品名":"鴻海", "股價": 150, "評等": "買進"}]
file_name = "ch02/files/stocks_2-1-1.csv"

#存取文件的步驟：1. 開啟/建立文件。2. 讀取/寫入文件。3. 關閉文件
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
