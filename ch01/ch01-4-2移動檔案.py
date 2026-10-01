#只搬移一個檔案
import os
import shutil
source = "today_spider.log" #來源檔案
target_dir = "history_logs" #目標資料夾
if not os.path.exists(target_dir):
   os.makedirs(target_dir)
   print(f"建立新資料夾: {target_dir}")

if os.path.exists(source):
   shutil.move(source, os.path.join(target_dir, "old.log"))
   print(f"已將 {source} 移動到 {target_dir}/old.log")
