#將 JSON 字串轉換為 Python 字典->記憶體操作
import json
raw_json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
# 模擬網路上抓下來的資料。將 JSON 字串轉換為 Python 字典，''單引號是python在用的
# key 必須是字串類型
data = json.loads(raw_json_str)
print(type(data))
print(data)
print(data['name'])
print(data['age'])

for key, value in data.items():
    print(f"{key}: {value}")
    
for item in data:
    print(data[item])