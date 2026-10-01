import os
import shutil


source = "today_spider.log"
target_dir = "history_logs"



if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"建立資料夾：{target_dir}")

if os.path.exists(source):
    shutil.move(source, os.path.join(target_dir, "old.log"))
    print("日誌已歸檔")



 

# 任務
# 1. 先用 py1-4.py 在主目錄下(例如C:\Users\User\python_idle_code)建立多個不同的檔案，例如
# 20260902_095049_data.txt
# 20260902_095539_data.txt
# 20260902_101029_data.txt

# 2. 透過 py1-4-1將這些檔案自動搬移到 history_logs 目錄
# 並自動修改檔名為
# old_20260902_095049_data.txt
# old_20260902_095539_data.txt
# old_20260902_101029_data.txt
