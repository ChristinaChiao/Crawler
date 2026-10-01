#將 Python 字典轉換為 JSON 字串->跟檔案操作有關
import json
import requests
# import warnings
# warnings.filterwarnings('ignore', message='Unverified HTTPS request')

url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/106/94b0e54b-ad45-4222-b26c-648773794ded.json?1130419174345"

try:
  response = requests.get(url, timeout=20, verify=False)
  response.raise_for_status()
  data = response.json()
except requests.exceptions.SSLerror as e:
  print("丟出requests.exceptions.SSLerror異常:", e)
  print(e)

# response = requests.get(url, timeout=20, verify=False) 
# #timeout=20：設定請求超時時間為20秒，verify=False：跳過SSL憑證驗證(該政府網站憑證不完整)
# response.raise_for_status()  # 檢查請求是否成功，如果不成功會引發 HTTPError 異常
# data = response.json()  #response.json()方法將回應內容解析為JSON格式，並返回一個Python字典或列表，具體取決於JSON的結構。

with open("ch02/files/clinic.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

#讀取json文件
with open("ch02/files/clinic.json", "r", encoding="utf-8") as f:
   loaded_data = json.load(f)
   for clinic in loaded_data: #loaded_data是列表，clinic是字典
     print(clinic["機構名稱"],clinic["電話"])
     print()
   print("-" * 30) 

  