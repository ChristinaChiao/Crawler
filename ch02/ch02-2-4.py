import json
raw_data = ''' 
{
  "status": "success",
  "results": [
    {"id":1, "info":{"name":"台北", "weather":"雨"}},
    {"id":2, "info":{"name":"台中", "weather":"晴"}}
    ],
  "demo":null
}
''' #第一層：字典，第二層：列表，第三層：字典，第四層：字典
try:
  data = json.loads(raw_data)  #將JSON字串轉換為Python字典
  print(data)
  print("台中天氣", data["results"][1]["info"]["weather"])  
except json.decoder.JSONDecodeError:
  print("json格式有錯")
except NameError:
  print("變數未定義")
except Exception:#越上層的類別盡量放後面
  print("丟出例外")

