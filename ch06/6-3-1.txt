import requests

url = "https://www.google.com"
res = requests.get(url)

if res.status_code == 200:
    print("請求成功，開始解析內容...")
elif res.status_code == 404:
    print("找不到網頁，請檢查網址是否有誤。")
else:
    print(f"出現其他狀況，狀態碼：{res.status_code}")
