#備份檔案到所在目錄並改名
import os
import shutil
from datetime import datetime #用來取得現在的時間：前面是模組名稱，後面是類別名稱

def backup_file(source_file, target_folder):  #定義一個函式，跟兩個參數
     if not os.path.exists(source_file): #來源檔案是否存在
          print(f"找不到來源檔案{source_file}") #f搭配{}，才會顯示變數
          return #提早離開
     try: #備份工作
          timestamp = datetime.now().strftime("%Y%m%d_%H%M") #命名複製檔案：創立現在的時間
          file_name = os.path.basename(source_file) 
          new_file_name = f"{timestamp}_{file_name}" #把前面兩個名字結合
          #組合完整的目標路徑
          destination = os.path.join(target_folder, new_file_name)
          shutil.copy2(source_file, destination) #執行複製
          print(f"備份成功!檔案已存至：{destination}")
     except Exception as e:
          print(f"備份失敗: {e}")
backup_file("data.txt", ".") #"所在目錄
