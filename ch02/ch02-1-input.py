import csv
import os

data = [{"品名":"台積電", "股價": 800, "評等": "買進"},
        {"品名":"聯發科", "股價": 1000, "評等": "持有"},
        {"品名":"鴻海", "股價": 150, "評等": "買進"}]
file_name = "ch02/files/stocks_2-1-try.csv"
# 存取文件的步驟
# 1. 開啟/建立文件
# 2. 讀取/寫入文件
# 3. 關閉文件

def save_csv(file_name, data): #file_name->檔案名稱, data->資料
    with open(file_name, mode = "w", encoding="utf-8-sig", newline="")as file:  
        #newline=""避免空行
        #第一個函數->儲存文件(stocks_2-1-try.csv)
        file_names = ["品名", "股價", "評等"]
        writer = csv.DictWriter(file, fieldnames=file_names) #將字典中的資料匯出為CSV
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_name): #file_name->檔案名稱
    with open(file_name, mode = "r", encoding="utf-8-sig")as file:
        #第二個函數->讀取文件(stocks_2-1-try.csv)
        reader = csv.DictReader(file) #變成字典格式
        for row in reader:
            print(row)

def append_csv(file_name):
    name = input("請輸入品名：")
    price = int(input("請輸入股價："))
    rating = input("請輸入評等：")
    
    new_data = {"品名": name, "股價": price, "評等": rating}
    not_exist = False
    
    if not os.path.exists(file_name):
        not_exist = True
    with open(file_name, mode = "a", encoding="utf-8-sig", newline="")as file: 
        #第三個函數->新增資料到文件(stocks_2-1-try.csv)
        file_names = ["品名", "股價", "評等"]
        writer = csv.DictWriter(file, fieldnames=file_names)
        if not_exist:
            writer.writeheader()
        writer.writerow(new_data)
        
save_csv(file_name, data)
while True:
    append_csv(file_name)
    read_csv(file_name)
    choice_yn = input("是否繼續？(y/n): ")
    if choice_yn == 'n':
        break