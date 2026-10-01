# import os
# folder = "." #當前資料夾
# picBox = [] #空的list，用來存放jpg檔案名稱

# def rename_files(picBox): #改名
#     for index, filename in enumerate(picBox): 
#         #enumerate是用來同時取得索引和值：index是索引，filename是值，picBox是列表
#         #建立新名字:cloth_0.jpg
#         new_name = f"cloth_{index}.jpg" #index代表第幾個jpg檔案
#         old_path = os.path.join(folder, filename) #舊的
#         new_path = os.path.join(folder, new_name) #新的
#         os.rename(old_path, new_path) #執行重新命名
#         print(f"已將 {old_path} 重新命名為 {new_path}")
  
# for files in os.listdir("."):
#     if os.path.isfile(files):
#         if "jpg" in files:
#             print(f"jpg檔案: {files}")
#             picBox.append(files) #將jpg檔案名稱加入picBox列表

# rename_files(picBox) #執行改名函式

import os
folder = "images" #圖片資料夾名稱
files = os.listdir(folder) #取得資料夾中的所有檔案名稱,並進行改名
for index, filename in enumerate(files): 
    new_name = f"pet_{index}.jpg" #index代表第幾個jpg檔案
    old_path = os.path.join(folder, filename) #舊的
    new_path = os.path.join(folder, new_name) #新的
    os.rename(old_path, new_path) #執行重新命名
    print(f"已將 {old_path} 重新命名為 {new_path}")