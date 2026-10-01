#將 Python 字典轉換為 JSON 字串->跟檔案操作有關
import json

config = {"url":"https://example.com", "retry":3}
with open("config.json", "w") as f:
    json.dump(config, f) 
    #config變數名稱，將字典轉換為JSON字串，並寫入檔案。
    #f為檔案物件，dump()方法將Python對象轉換為JSON格式並寫入文件
    
with open("config.json", "r") as f: #讀取文件
   loaded_config = json.load(f) #loaded_config變數名稱
   print(f"網址是 {loaded_config['url']}")