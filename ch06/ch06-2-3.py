import requests

url = "https://httpbin.org/post"

payload = {
    "keyword": "Python課程",
    "page":2
}

response = requests.post(url, data=payload)
if response.status_code == 200:
    json_data = response.json()
    print("伺服器收到的資料(form):", json_data["form"])
    print("伺服器收到的資料(json):", json_data["json"])
else:
    print("Failed to send POST request. Status code:", response.status_code)
    
    
