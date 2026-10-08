# 天氣API
import requests 
def get_api_key():
    with open("C:/venvShao/PythonCode/ch04/mykey.txt", "r") as file:
        return file.read().strip()
url = "http://api.openweathermap.org/data/2.5/weather?lat=24.990150143617672&lon=121.31375335452226&appid=" + get_api_key()
response = requests.get(url)
data = response.json()
print(data)
temp = round(data["main"]["temp"] - 273.15, 1)
temp_min = round(data["main"]["temp_min"] - 273.15, 1)
temp_max = round(data["main"]["temp_max"] - 273.15, 1)  
deg = data["wind"]["deg"]


print("目前溫度：", temp) #273.15是攝氏零度對應的開氏溫度，轉換為攝氏溫度
print("最低溫度：", temp_min) 
print("最高溫度：", temp_max)
print("風向：", deg) 
if deg == 0: #0 表示北風，90度表示東風，180度表示南風，270度表示西風
    print("北風")
elif deg == 90:
    print("東風")
elif deg == 180:
    print("南風")
elif deg == 270:
    print("西風")