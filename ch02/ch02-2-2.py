#將 Python 字典轉換為 JSON 字串->記憶體操作
import json

student_info ={
  "id":"A123",
  "course":["Python", "爬蟲", "AI"],
  "is_graduated": False
}

out_json = json.dumps(student_info, ensure_ascii=False, indent=4) 
#將字典轉換為JSON字串，ensure_ascii=False避免中文亂碼，indent=4縮排4個空格
print(type(out_json))
print(out_json)