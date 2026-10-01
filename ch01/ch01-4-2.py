#搬移所有含有data名字的txt檔案到history_logs資料夾
# import os
# import shutil
# from glob import glob
# source = "*data*.txt" #含有data名字的檔案
# target_dir = "history_logs" #放置的目標資料夾

# for source in glob("*data*.txt"):
#     if os.path.exists(source):
#         shutil.move(source, os.path.join(target_dir, f"old_{source}"))
#         print(f"已將 {source} 移動到 {target_dir}/old_{source}")
        
import os
import shutil
target_dir = "history_logs" #目標資料夾
def move_files(source):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"建立新資料夾: {target_dir}")
    if os.path.exists(source):
        shutil.move(source, os.path.join(target_dir, f"old_{source}"))
        print(f"已將 {source} 移動到 {target_dir}/old_{source}")
        
print(os.listdir(".")) #查看目前目錄下的所有檔案與資料夾
for f in os.listdir("."):
    if os.path.isfile(f):
        print(f"檔案: {f}")
        if "txt" in f:
            print(f"是txt檔案: {f}")
            move_files(f)
            print(f"已處理檔案: {f}")
    elif os.path.isdir(f):
        print(f"資料夾: {f}")
    