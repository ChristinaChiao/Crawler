
#使用pandas，算平均溫度
import pandas as pd

df = pd.DataFrame(
  {
    "city": ["Taipei", "Taichung", "Kaohsiung"],
     "temperature": [30, 28, 32]
  } 
)
print(df)
print("平均溫度：", round(df["temperature"].mean(),1))

#真實的天氣資料
import pandas as pd
import json

with open(r"C:\Users\User\venvShao\PythonCode\ch03\F-C0032-027.json", encoding="utf-8") as f:
     data = json.load(f)
     print(data)
     print()
     print("溫度：", data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
     print()  

#縣市最小溫度、最大溫度
df = pd.DataFrame(data)
print("縣市名稱：", df["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度：", df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

temp_data = df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1]
start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度：", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度：", temp_data[start:end])
print()
