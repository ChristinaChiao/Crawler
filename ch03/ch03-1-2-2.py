#使用pandas，算五個縣市最大、最小及平均溫度，方式
import pandas as pd
import json

files = ["F-C0032-010.json", "F-C0032-013.json", "F-C0032-018.json", "F-C0032-026.json", "F-C0032-027.json"]
path = r"C:\Users\User\venvShao\PythonCode\ch03"
for file in files: #file的意思是目前正在處理的檔案名稱，files裡面有幾筆就會跑幾次
  full_path = path + "\\" + file
  with open(full_path, encoding="utf-8") as f:
    data = json.load(f)
  df = pd.DataFrame(data)
  print("縣市名稱：", df["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
  temp_data = df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1]
  
  startMin = temp_data.index("溫")+1
  endMin = temp_data.index("至")
  print("最小溫度：", temp_data[startMin:endMin])
  
  startMax = temp_data.index("至")+1
  endMax = temp_data.index("度")
  print("最大溫度：", temp_data[startMax:endMax]) 
  
  print("平均溫度：", round((int(temp_data[startMin:endMin]) + int(temp_data[startMax:endMax])) / 2, 1))
  print()
  